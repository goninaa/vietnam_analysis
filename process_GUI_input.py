import attr
from attr.validators import instance_of
from pathlib import Path
from typing import Union
import os
import ntpath

@attr.s(frozen=True)
class TxtFile:
    """File objects with path attribute and several metadata attributes.
    Instantiated by the ProcessFilelist class, passed to the ProcessData class
    Attributes: path, fname, experiment.
    """
    path = attr.ib(validator=instance_of(Path))
    fname = attr.ib(validator=instance_of(str))
    fstart = attr.ib(validator=instance_of(str))
    experiment = attr.ib(validator=instance_of(str))
    hour = attr.ib(validator=instance_of(str))
    minutes = attr.ib(validator=instance_of(str))
    seconds = attr.ib(validator=instance_of(str))
    

@attr.s
class ProcessFilelist:
    """Pipeline to process a list of files.
    Reads attributes from filename and creates a list of TxtFile objects to pass.
    Attributes: filelist, invalid_files, txt_dict.
    Methods: instantiate_txt_file, assert_csv, extract_file_attrs.
    """
    filelist = attr.ib(validator=instance_of(list))
    invalid_files = attr.ib(default=attr.Factory(list)) ### should add invalid files output ###
    txt_dict = attr.ib(default=attr.Factory(dict)) # dict of TxtFile instances to pass forward

    def get_file_attrs(self) -> None:
        """Analizes file attributes and instantiate TxtFile objects"""
        for txtfile in self.filelist:
            path = Path(txtfile)
            fname = path.name
            if not self.assert_txt(path): # accepts only .txt files
                self.invalid_files.append(fname)
                continue
            
            fattrs = self.extract_file_attrs(fname)
            if not fattrs: # accepts files only if named in the appropriate pattern
                self.invalid_files.append(fname)
                continue
            hour, minutes, seconds = fattrs[0], fattrs[1], fattrs[2]
            fstart = f'{hour}:{minutes}:{seconds}'
            experiment = os.path.basename(os.path.dirname(path))
            # head, tail = os.path.split(path)
            # experiment = head
            self.instantiate_txt_file(path, fname, experiment, fstart, hour, minutes, seconds)
    
    def assert_txt(self, path: Path) -> bool:
        """Asserts that a file is a csv file"""
        return str.lower(path.suffix) == '.txt'
    
    def extract_file_attrs(self, fname: str) -> Union[list, bool]:
        """If the file named appropriately, extracts its attributes from filename"""
        fattrs = fname.split('_')
        return fattrs
        # return fattrs if len(fattrs) == 10 else False
        
    def instantiate_txt_file(self, path: Path, fname: str, experiment: str, fstart: str, hour, minutes, seconds) -> TxtFile:
        """Instantiates TxtFile objects"""
        txt_item = TxtFile(path=path, fname=fname, experiment=experiment, fstart = fstart, hour = hour, minutes = minutes, seconds = seconds)
        try:
            self.txt_dict[f'{fname}'] = txt_item
        except KeyError:
            self.txt_dict[f'{fname}'] = {fname: txt_item}


if __name__ == "__main__":
    filelist = ['new_labeled_data_11082019_22⁩/11_30_5__11_31_50.txt']
    # filelist = ['11_30_5__11_31_50.txt']
    files = ProcessFilelist(filelist)
    files.get_file_attrs()
    print(files.txt_dict)
    # print(files.invalid_files)