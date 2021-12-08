import h5py

def PrintOnlyDataset(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name)
        
def PrintData(hdfpath):
    with h5py.File(hdfpath,'r') as f:
        f.visititems(PrintOnlyDataset)  





