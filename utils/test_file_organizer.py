import unittest
import os
import tempfile
import shutil
from pathlib import Path
from .file_organizer import organize_files

class TestFileOrganizer(unittest.TestCase):
    def setUp(self):
        """Create a temporary directory for testing"""
        self.test_dir = Path(tempfile.mkdtemp())
        self.in_dir = self.test_dir / "in"
        self.out_dir = self.test_dir / "out"
        
    def tearDown(self):
        """Clean up the temporary directory after each test"""
        shutil.rmtree(self.test_dir)
        
    def test_create_folders(self):
        """Test that 'in' and 'out' folders are created"""
        result = organize_files(str(self.test_dir))
        self.assertTrue(result)
        self.assertTrue(self.in_dir.exists())
        self.assertTrue(self.out_dir.exists())
        
    def test_move_jpg_files(self):
        """Test that .jpg files are moved to 'in' folder"""
        # Create test .jpg files
        jpg_file1 = self.test_dir / "test1.jpg"
        jpg_file2 = self.test_dir / "test2.jpg"
        jpg_file1.write_text("fake jpg content")
        jpg_file2.write_text("fake jpg content")
        
        # Create a non-jpg file to ensure it's not moved
        txt_file = self.test_dir / "test.txt"
        txt_file.write_text("fake txt content")
        
        result = organize_files(str(self.test_dir))
        self.assertTrue(result)
        
        # Check that .jpg files were moved
        self.assertTrue((self.in_dir / "test1.jpg").exists())
        self.assertTrue((self.in_dir / "test2.jpg").exists())
        
        # Check that non-jpg files were not moved
        self.assertTrue((self.test_dir / "test.txt").exists())
        self.assertFalse((self.in_dir / "test.txt").exists())
        
    def test_move_docx_files(self):
        """Test that .docx files are moved to 'out' folder"""
        # Create test .docx files
        docx_file1 = self.test_dir / "test1.docx"
        docx_file2 = self.test_dir / "test2.docx"
        docx_file1.write_text("fake docx content")
        docx_file2.write_text("fake docx content")
        
        # Create a non-docx file to ensure it's not moved
        txt_file = self.test_dir / "test.txt"
        txt_file.write_text("fake txt content")
        
        result = organize_files(str(self.test_dir))
        self.assertTrue(result)
        
        # Check that .docx files were moved
        self.assertTrue((self.out_dir / "test1.docx").exists())
        self.assertTrue((self.out_dir / "test2.docx").exists())
        
        # Check that non-docx files were not moved
        self.assertTrue((self.test_dir / "test.txt").exists())
        self.assertFalse((self.out_dir / "test.txt").exists())
        
    def test_nonexistent_directory(self):
        """Test handling of nonexistent directory"""
        nonexistent_dir = "/this/directory/does/not/exist"
        result = organize_files(nonexistent_dir)
        self.assertFalse(result)
        
    def test_file_with_subdirectories(self):
        """Test that subdirectories are not affected"""
        # Create a subdirectory with files
        subdir = self.test_dir / "subdir"
        subdir.mkdir()
        subdir_file = subdir / "test.jpg"
        subdir_file.write_text("fake jpg content")
        
        result = organize_files(str(self.test_dir))
        self.assertTrue(result)
        
        # Check that subdirectory files were not moved
        self.assertTrue(subdir_file.exists())
        self.assertFalse((self.in_dir / "test.jpg").exists())

if __name__ == '__main__':
    unittest.main()