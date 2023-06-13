import torch
import clip # type: ignore
from glob import glob
from PIL import Image
from PIL.Image import Image as ImageType
from app.log import logger

logger.info('Loading images...')
IMAGE_DIR: str = "/app/services/val2014"
FILEPATHS = glob(f'{IMAGE_DIR}/*.jpg')
logger.info(f'Found {len(FILEPATHS)} images')


class ImageSearcher():

    def __init__(
        self,
        model_name: str = "ViT-B/32",
    ):
        
        logger.info('Loading CLIP model...')
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load(model_name, device=device)
        
        logger.info('Loading image vectors...')
        self.image_vectors = torch.cat(
            [self.get_vector_for_image(Image.open(filepath)) for filepath in FILEPATHS]
        )
        self.image_vectors /= self.image_vectors.norm(dim=-1,keepdim=True)


    def get_vector_for_text(self, text: str):
        with torch.no_grad():
            vector = self.model.encode_text(clip.tokenize(text))
        return vector

    def get_vector_for_image(self, image: ImageType):
        with torch.no_grad():
            vector = self.model.encode_image(self.preprocess(image).unsqueeze(0))
        return vector
    
    def search(self, text: str):
        scores = self.image_vectors @ self.get_vector_for_text(text).t()
        return scores.squeeze().argsort(descending=True)[:10]

class DummyImageSearcher():

    def search(self, text: str):
        result = []
        for i in range(10):
            result.append((hash(text) % 328 + i*32) % 328)
        return torch.IntTensor(result)
    
searcher = ImageSearcher()
# searcher = DummyImageSearcher()
