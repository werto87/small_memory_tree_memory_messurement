from conan import ConanFile


class Project(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def configure(self):
        # We can control the options of our dependencies based on current options
        self.options["catch2"].with_main = True
        self.options["catch2"].with_benchmark = True
        self.options["boost"].header_only = True

    def requirements(self):
        # self.requires("catch2/2.13.7")
        # self.requires("boost/1.83.0", force=True)
        # self.requires("confu_json/1.0.0")
        # self.requires("soci/4.0.3")
        self.requires("st_tree/1.2.2")