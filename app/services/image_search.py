import torch
import clip # type: ignore
from glob import glob
from PIL import Image
from PIL.Image import Image as ImageType


class ImageSearcher():

    def __init__(
        self,
        model_name: str = "ViT-B/32",
        image_dir: str = "./val2014"
    ):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(model_name, device=device)
        filepaths = glob(f'{image_dir}/*.jpg')
        self.image_vectors = torch.cat(
            [self.get_vector_for_image(Image.open(filepath)) for filepath in filepaths]
        )
        self.image_vectors /= self.image_vectors.norm(dim=-1,keepdim=True)


    def _encode_text(self, text: str):
        return self.model.encode_text(clip.tokenize(text))


    def search(self, text: str):
        scores = self.image_vectors @ self._encode_text(text).t()
        return scores.squeeze().argsort(descending=True)[:10]


    def get_vector_for_image(self, image: ImageType):
        return self.model.encode_image(self.preprocess(image).unsqueeze(0))

searcher = ImageSearcher()
