from subprocess import check_call
from pathlib import Path


def dicom_to_nifti(source_folder: Path, target_folder: Path, name=None):
    """Converts folder of dicoms into a nii.gz file."""
    cmd = ['dcm2niix', '-z', 'y']
    if name is not None:
        cmd.append('-f')
        cmd.append(name)
    cmd.append('-o')
    cmd.append(f'{str(target_folder)}/')
    cmd.append(f'{str(source_folder)}/')
    return check_call(cmd)


