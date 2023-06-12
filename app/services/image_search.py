import torch
import clip # type: ignore
from glob import glob
from PIL import Image
from PIL.Image import Image as ImageType
from app.log import logger


class ImageSearcher():

    def __init__(
        self,
        model_name: str = "ViT-B/32",
        image_dir: str = "/app/services/val2014"
    ):
        logger.info('Loading images...')
        filepaths = glob(f'{image_dir}/*.jpg')
        logger.info(f'Found {len(filepaths)} images')

        logger.info('Loading CLIP model...')
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(model_name, device=device)
        
        logger.info('Loading image vectors...')
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

class DummyImageSearcher():

    def search(self, text: str):
        return torch.randint(327, (10,))

# searcher = ImageSearcher()
searcher = DummyImageSearcher()

