import os
import shutil


class SiteBuilder:
    def __init__(self, templates_dir: str, output_dir: str) -> None:
        self.templates_dir = templates_dir
        self.output_dir = output_dir

    def build_site(self) -> None:
        os.makedirs(self.output_dir, exist_ok=True)
        for name in os.listdir(self.templates_dir):
            src = os.path.join(self.templates_dir, name)
            dst = os.path.join(self.output_dir, name)
            if os.path.isfile(src):
                shutil.copy(src, dst)


if __name__ == "__main__":
    builder = SiteBuilder("templates", "dist")
    builder.build_site()
