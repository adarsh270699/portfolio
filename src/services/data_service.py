import json
import os
from typing import Dict, Any, Optional

class DataService:
    """Service class for handling data operations"""
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.data_folder = self._get_data_folder()
       
    
    def _get_data_folder(self) -> str:
        """Get data folder from config"""
        if self.config and 'DATA_FOLDER' in self.config:
            return self.config['DATA_FOLDER']
        return 'src/data'
    
    def load_json_file(self, filename: str) -> Dict[str, Any]:
        """
        Load data from a JSON file
        
        Args:
            filename (str): Name of the JSON file
            
        Returns:
            Dict: Loaded JSON data
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        file_path = os.path.join(self.data_folder, filename)
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {filename}: {str(e)}", e.doc, e.pos)
    
    def get_contact_info(self) -> Dict[str, Any]:
        """
        Get contact information from JSON file
        
        Returns:
            Dict: Contact information data
        """
        filename = self._get_contact_info_filename()
        return self.load_json_file(filename)
    
    def get_content(self) -> Dict[str, Any]:
        """
        Get content data from JSON file
        
        Returns:
            Dict: Content data
        """
        filename = self._get_content_filename()
        return self.load_json_file(filename)
    
    def _get_contact_info_filename(self) -> str:
        """Get contact info filename from config"""
        if self.config and 'CONTACT_INFO_FILE' in self.config:
            return self.config['CONTACT_INFO_FILE']
        return 'contact-info.json'
    
    def _get_content_filename(self) -> str:
        """Get content filename from config"""
        if self.config and 'CONTENT_FILE' in self.config:
            return self.config['CONTENT_FILE']
        return 'content.json'
    
    def get_all_data(self) -> Dict[str, Any]:
        """
        Get all data files as a combined dictionary
        
        Returns:
            Dict: Combined data from all JSON files
        """
        try:
            return {
                'contact_info': self.get_contact_info(),
                'content': self.get_content()
            }
        except Exception as e:
            # Return empty data if files can't be loaded
            return {
                'contact_info': {},
                'content': {}
            } 