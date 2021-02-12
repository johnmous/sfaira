import os
from typing import Union
from .base import Dataset_d10_1016_j_cell_2018_02_001


class Dataset(Dataset_d10_1016_j_cell_2018_02_001):

    def __init__(
            self,
            data_path: Union[str, None] = None,
            meta_path: Union[str, None] = None,
            cache_path: Union[str, None] = None,
            **kwargs
    ):
        super().__init__(data_path=data_path, meta_path=meta_path, cache_path=cache_path, **kwargs)
        self.id = "mouse_bone_2018_microwell-seq_han_001_10.1016/j.cell.2018.02.001"
        self.organ = "bone tissue"

        self.class_maps = {
            "0": {
                "B cell_Igkc high(Bone-Marrow)": "naive B cell",
                "Dendritic cell_H2-Eb1 high(Bone-Marrow)": "dendritic cell",
                "Dendritic cell_Siglech high(Bone-Marrow)": "dendritic cell",
                "Macrophage_Ms4a6c high(Bone-Marrow)": "macrophage",
                "Macrophage_S100a4 high(Bone-Marrow)": "macrophage",
                "Erythroblast(Bone-Marrow)": "erythroid progenitor",
                "Mast cell(Bone-Marrow)": "mast cell",
                "Monocyte_Mif high(Bone-Marrow)": "monocyte",
                "Monocyte_Prtn3 high(Bone-Marrow)": "monocyte",
                "Neutrophil progenitor(Bone-Marrow)": "neutrophil progenitor",
                "Neutrophil_Cebpe high(Bone-Marrow)": "neutrophil",
                "Neutrophil_Fcnb high(Bone-Marrow)": "neutrophil",
                "Neutrophil_Mmp8 high(Bone-Marrow)": "neutrophil",
                "Neutrophil_Ngp high(Bone-Marrow)": "neutrophil",
                "Hematopoietic stem progenitor cell(Bone-Marrow)": "hematopoietic precursor cell",
                "Pre-pro B cell(Bone-Marrow)": "early pro-B cell",
                "T cell_Ms4a4b high(Bone-Marrow)": "CD4-positive, alpha-beta T cell"
            },
        }

    def _load(self):
        self._load_generalized(samplename="BoneMarrow1_dge")
