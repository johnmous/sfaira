import os
from typing import Union
from .external import DatasetBase
from .external import ADATA_IDS_SFAIRA
import anndata
import numpy as np


class Dataset(DatasetBase):
    """
    This data loader supports reading of the downloaded raw data file if `load_raw=True` is passed to self.load()
    To download the datafile required by this dataloader, use the link provided as the `download_website` attribute of
    this class. For (up to 100-fold faster) repeated data loading, please pass `load_raw=False` when calling the
    self.load() method. For this, you need to preprocess the raw files as below and place the resulting h5ad file in the
    data folder of this organ:

    import anndata
    import numpy as np
    adata = anndata.read_loom('c95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.loom')
    idx = np.logical_and((adata.obs['derived_organ_parts_label'] == 'umbilical cord blood').values, (adata.obs['emptydrops_is_cell'] == 't').values)
    adata = adata[idx].copy()
    adata.write('ica_bone.h5ad')

    :param path:
    :param meta_path:
    :param kwargs:
    """

    def __init__(
            self,
            path: Union[str, None] = None,
            meta_path: Union[str, None] = None,
            **kwargs
    ):

        DatasetBase.__init__(self=self, path=path, meta_path=meta_path, **kwargs)
        self.species = "human"
        self.id = "human_blood_2018_10x_ica_001_unknown"
        self.download_website = "https://data.humancellatlas.org/project-assets/project-matrices/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.loom"
        self.organ = "blood"
        self.sub_tissue = "umbilical_cord_blood"
        self.has_celltypes = False

        self.class_maps = {
            "0": {},
        }

    def _load(self, fn=None):
        if fn is None and self.path is None:
            raise ValueError("provide either fn in load or path in constructor")

        if self._load_raw:
            if fn is None:
                fn = os.path.join(self.path, "human/blood/cc95ff89-2e68-4a08-a234-480eca21ce79.homo_sapiens.loom")
            self.adata = anndata.read_loom(fn)
            idx = np.logical_and((self.adata.obs['derived_organ_parts_label'] == 'umbilical cord blood').values,
                                 (self.adata.obs['emptydrops_is_cell'] == 't').values)
            self.adata = self.adata[idx].copy()

        else:
            if fn is None:
                fn = os.path.join(self.path, "human/blood/ica_blood.h5ad")
            self.adata = anndata.read(fn)

        self.adata.uns[ADATA_IDS_SFAIRA.author] = 'Regev'
        self.adata.uns[ADATA_IDS_SFAIRA.year] = 2018
        self.adata.uns[ADATA_IDS_SFAIRA.doi] = None
        self.adata.uns[ADATA_IDS_SFAIRA.protocol] = '10x'
        self.adata.uns[ADATA_IDS_SFAIRA.organ] = self.organ
        self.adata.uns[ADATA_IDS_SFAIRA.subtissue] = self.sub_tissue
        self.adata.uns[ADATA_IDS_SFAIRA.animal] = "human"
        self.adata.uns[ADATA_IDS_SFAIRA.id] = self.id
        self.adata.uns[ADATA_IDS_SFAIRA.wget_download] = self.download_website
        self.adata.uns[ADATA_IDS_SFAIRA.has_celltypes] = self.has_celltypes
        self.adata.uns[ADATA_IDS_SFAIRA.normalization] = 'raw'

        self.adata.obs[ADATA_IDS_SFAIRA.cell_ontology_class] = None
        self.adata.obs[ADATA_IDS_SFAIRA.healthy] = True
        self.adata.obs[ADATA_IDS_SFAIRA.state_exact] = 'healthy'

        self._convert_and_set_var_names(symbol_col='index', ensembl_col='Accession', new_index=ADATA_IDS_SFAIRA.gene_id_ensembl)
