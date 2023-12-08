package filerename

import (
	"io/ioutil"
	"os"
	"path/filepath"
	"strings"
)

// RenameFiles takes a directory path and a function for renaming a file as input.
// It goes through each PDF file in the directory, uses the renaming function to get the new name, and renames the file.
func RenameFiles(dirPath string, renameFunc func(string) (string, error)) error {
	files, err := ioutil.ReadDir(dirPath)
	if err != nil {
		return err
	}

	for _, file := range files {
		if file.IsDir() {
			continue
		}

		if filepath.Ext(file.Name()) != ".pdf" {
			continue
		}

		oldPath := filepath.Join(dirPath, file.Name())
		newName, err := renameFunc(file.Name())
		if err != nil {
			return err
		}

		newPath := filepath.Join(dirPath, newName)
		err = os.Rename(oldPath, newPath)
		if err != nil {
			return err
		}
	}

	return nil
}

// RemoveExtension removes the file extension from a file name.
func RemoveExtension(fileName string) string {
	return strings.TrimSuffix(fileName, filepath.Ext(fileName))
}