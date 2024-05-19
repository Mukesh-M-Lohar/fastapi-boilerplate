# add_service.py

import os
import sys


def add_service(service_name):
    # Convert service_name to lowercase
    service_name_lower = service_name.strip().lower()

    # Convert service_name to PascalCase
    service_name_pascal = "".join(word.capitalize() for word in service_name.split("_"))

    # Define directory structure
    directories = ["__init__.py", "api", "db_ops.py", "db_table.py", "schema.py"]

    # Create parent folder
    parent_folder = os.path.join("edusmart", service_name_lower)
    os.makedirs(parent_folder, exist_ok=True)

    # Create directories
    for directory in directories:
        directory_path = os.path.join(parent_folder, directory)
        if not os.path.exists(directory_path):
            if not directory.endswith(
                ".py"
            ):  # Exclude Python file creation for non-API directories
                os.makedirs(directory_path)
            else:
                with open(directory_path, "w"):
                    continue

    # Create API directory and files
    api_directory = os.path.join(parent_folder, "api", service_name_lower)
    os.makedirs(api_directory, exist_ok=True)
    api_files = ["__init__.py", f"{service_name_lower}_api.py"]
    for file in api_files:
        file_path = os.path.join(api_directory, file)
        if not os.path.exists(file_path):
            with open(file_path, "w"):
                pass

    print(f"Service '{service_name_pascal}' added successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_service.py <service_name>")
        sys.exit(1)

    service_name = sys.argv[1]
    add_service(service_name)
