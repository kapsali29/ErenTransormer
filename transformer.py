import logging
import os
import sys

import pandas as pd

from settings import DATASET_ORDER_DICT

logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
log = logging.getLogger(__name__)


class ErenLangMapping(object):
    def __init__(self):
        self.dataset_folder = 'DATA/'

    @staticmethod
    def check_if_file_exists(path):
        """
        This function is used to test if the provided file path exists
        Args:
            path: dataset path

        Returns: True if dataset exists False if Not
        """
        result = os.path.exists(path)
        if not result:
            log.info("File: {} does not exists inside DATA folder".format(path))
        return result

    @staticmethod
    def create_output_folder():
        """This function is used to create output folder"""
        if not os.path.exists('OUTPUT'):
            os.makedirs('OUTPUT')

    @staticmethod
    def store_output_dataset(data, full_path):
        """
        This function is used to store provided dataframe to output folder
        Args:
            data: pandas dataframe
            full_path: data path

        Returns: stores in OUTPUT folder the translated pandas dataFrame

        """
        base_name = os.path.basename(full_path)
        output_file_path = os.path.join('OUTPUT', base_name)
        data.to_csv(output_file_path, sep=';', index=False)
        log.info('{} stored'.format(output_file_path))

    def transform_lang(
            self,
            path,
            separator,
            dataset_values_dict,
            dataset_columns_dict
    ):
        """
        This function is used to translate mapped values from spanish to engish using stored dictionaries

        Args:
            path: dataset path
            separator: csv separator
            dataset_values_dict: values mapping dictionary
            dataset_columns_dict: columns mapping dictionary

        Returns: Translated dataset

        """
        file_exists = self.check_if_file_exists(path)
        if file_exists:
            data = pd.read_csv(path, sep=separator)
            for key in dataset_values_dict.keys():
                data[key] = data[key].map(dataset_values_dict[key])
            data = data.rename(columns=dataset_columns_dict)
            print(data)
            return data
        else:
            return None

    def call_transformation(self):
        """This function is the generic executioner of this class"""
        log.info('Create OUTPUT folder if not exists')
        self.create_output_folder()

        for obj in DATASET_ORDER_DICT:
            log.info(obj['msg'])
            path = obj['path']
            data = self.transform_lang(
                path=path,
                separator=';',
                dataset_values_dict=obj['dataset_values_dict'],
                dataset_columns_dict=obj['dataset_columns_dict']
            )
            self.store_output_dataset(data, path)


if __name__ == '__main__':
    mapping = ErenLangMapping()
    mapping.call_transformation()
