from typing import Tuple

import pytorch_lightning as pl
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm


@torch.no_grad()
def model_evaluate(model: pl.LightningModule, test_loader: DataLoader) -> Tuple[int, int]:
    """Evaluate model with specified test dataset.

    * Evaluation without torch.grad calculations.

    Parameters
    ----------
    model: pl.LightningModule
        Trained model in inference mode.
    test_loader: DataLoader
        Test dataset to be evaluated on.
    Returns
    -------
    correct: int
        Count of correct predictions.
    total: int
        Count of all items.
    """

    correct = 0
    total = 0
    for img, label in tqdm(test_loader):
        pred = model(img).detach().cpu()

        correct += (pred.argmax(dim=1) == label).sum()
        total += pred.size(0)

    return correct, total
