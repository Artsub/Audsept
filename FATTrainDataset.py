class FATTrainDataset(Dataset):
	def __init__(self, mel_curated, mel_noisy, _transforms):
		super().__init__()
		self.mel_curated = mel_curated
		self.mel_noisy = mel_noisy
		self.transforms = _transforms

	def __len__(self):
		return len(self.mel_curated) + len(self.mel_noisy)

	def __getitem__(self, idx):
		image_curated = Image.fromarray(self.mel_curated[idx], mode='RGB')
		time_dim, base_dim = image_curated.size
		crop = random.randint(0, time_dim - base_dim)
		image_curated = image_curated.crop((crop, 0, crop + base_dim, base_dim))
		image_curated = self.transforms(image_curated).div_(255)

		image_noisy = Image.fromarray(self.mel_noisy[idx], mode='RGB')
		time_dim, base_dim = image_noisy.size
		crop = random.randint(0, time_dim - base_dim)
		image_noisy = image_noisy.crop((crop, 0, crop + base_dim, base_dim))
		image_noisy = self.transforms(image_noisy).div_(255)
		return image_curated, image_noisy
