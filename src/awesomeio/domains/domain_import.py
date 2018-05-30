from pathlib import Path
from importlib import import_module
import os

domains_path = Path(__file__).parent
for path in domains_path.glob('definitions/**/*.py'):
    rel_path = path.relative_to(domains_path)
    module_name, _ = os.path.splitext(str(rel_path))
    module_name = module_name.replace(os.path.sep, '.')
    module_name = f"awesomeio.domains.{module_name}"
    import_module(module_name)
