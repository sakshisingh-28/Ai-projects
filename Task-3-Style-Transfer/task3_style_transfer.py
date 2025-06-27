from PIL import Image
import torchvision.transforms as transforms

def load_image(img_path, max_size=512):
    image = Image.open(img_path).convert('RGB')
    size = min(max(image.size), max_size)
    transform = transforms.Compose([
        transforms.Resize((size, size)),
        transforms.ToTensor()
    ])
    image = transform(image)[:3, :, :].unsqueeze(0)
    return image

# Load your content and style images here to apply style transfer
