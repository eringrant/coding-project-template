# coding-project-template

This repository template is useful for developing research-oriented coding projects as Python packages.

## Citation

To cite the work that this code is associated with, use:

```
@inproceedings{TODO_citation_key,
  title={TODO},
  author={TODO},
  booktitle={TODO},
  year={TODO}
}
```

## Quickstart

Clone the repo:

```sh
git clone git@github.com:eringrant/coding-project-template.git
cd coding-project-template/
```

To install a Conda environment with the requisite packages **on CPU**:

```sh
conda env create --file environment-cpu.yml
```

To test that the package can be imported successfully:

```sh
conda activate TODO_package_name
python -c "import TODO_package_name"
```

## Setup

### Installing packages

Any of the following installation methods will allow you to activate the environment with
`conda activate TODO_package_name`.

#### Option #1: Conda install (CPU-only)

To install via [Mamba](https://mamba.readthedocs.io/) (recommended)
or [Conda](https://docs.conda.io/), do:

```sh
conda env create --file environment-cpu.yml
```

#### Option #2: Conda install on GPU on a local machine

To install via [Mamba](https://mamba.readthedocs.io/) (recommended)
or [Conda](https://docs.conda.io/) with GPU support, do:

```sh
conda env create --file environment-gpu.yml
```

#### Option #3: Conda install on GPU on a SLURM cluster

If working on the head node of a SLURM cluster, you will need
to create a GPU-compatible environment on a compute node with an available GPU via:

```sh
srun --partition=gpu --gres=gpu:1 conda env create -f environment-gpu.yml
```

Note that you may have to adapt the `partition` name to the available partitions on your cluster;
run `sinfo -s` to display details about partitions.

### Storage locations

To avoid using up too much disk space in your home directory, make sure to point some packages to
alternative locations by adding the following to a shell configuration file, such as
`~/.bashrc` or `~/.zshrc`. (Remember to replace the ellipsis `...` with your desired locations!)

```sh
# Transient output.
export SCRATCH_HOME="..."
```

## Devtools

### Pre-commit

[`.pre-commit-config.yaml`](/.pre-commit-config.yaml) has been configured to run several autoformatters,
including the [Black](https://black.readthedocs.io/) autoformatter as well as [Flake8](https://flake8.pycqa.org/).
Run the following to install, update, and cache all pre-commit tools:

```bash
pre-commit install && pre-commit run
```
