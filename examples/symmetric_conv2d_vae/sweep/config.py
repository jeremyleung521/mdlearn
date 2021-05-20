from pathlib import Path
from typing import Optional, List, Tuple
from mdlearn.utils import BaseSettings, OptimizerConfig, SchedulerConfig


class SymmetricConv2dVAEConfig(BaseSettings):

    # Path to HDF5 training file
    input_path: Path = Path("TODO")
    # Input image shapes
    input_shape: Tuple[int, ...] = (1, 28, 28)
    # Name of the dataset in the HDF5 file.
    dataset_name: str = "contact_map"
    # Name of scalar datasets in the HDF5 file.
    scalar_dset_names: List[str] = []
    # Name of optional values field in the HDF5 file.
    values_dset_name: Optional[str] = None
    # Sets requires_grad torch.Tensor parameter for scalars specified
    # by scalar_dset_names. Set to True, to use scalars for multi-task
    # learning. If scalars are only required for plotting, then set it as False.
    scalar_requires_grad: bool = False
    # Whether to pull all the training data into memory or read each
    # batch from disk on the fly
    in_memory: bool = True
    # Percentage of data to be used as training data after a random split.
    split_pct: float = 0.8
    # Random seed for shuffling train/validation data
    seed: int = 333
    # Whether or not to shuffle train/validation data
    shuffle: bool = True
    # Number of epochs to train
    epochs: int = 10
    # Training batch size
    batch_size: int = 64
    # Gradient clipping (max_norm parameter of torch.nn.utils.clip_grad_norm_)
    clip_grad_max_norm: float = 5.0
    # Pretrained model weights
    init_weights: Optional[str] = None
    # Optimizer params
    optimizer: OptimizerConfig = OptimizerConfig(name="Adam", hparams={"lr": 0.0001})
    # Learning rate scheduler params
    scheduler: Optional[SchedulerConfig] = None

    # Model hyperparameters
    latent_dim: int = 64
    filters: List[int] = [100, 100, 100, 100]
    kernels: List[int] = [5, 5, 5, 5]
    strides: List[int] = [1, 2, 1, 1]
    latent_dim: int = 10
    affine_widths: List[int] = [64]
    affine_dropouts: List[float] = [0.0]
    activation: str = "ReLU"
    output_activation: str = "Sigmoid"  # None is Identity function
    lambda_rec: float = 1.0

    # Training settings
    # Number of data loaders for training
    num_data_workers: int = 0
    # Whether or not to ignore the GPU while training.
    ignore_gpu: bool = False


if __name__ == "__main__":
    SymmetricConv2dVAEConfig().dump_yaml("symmetric_conv2d_vae_sweep_default.yaml")
