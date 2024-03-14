from pydantic import BaseModel


class ProjectInformation(BaseModel):
    _project_name: str

    @property
    def projectname(self):
        return self._project_name

    @projectname.setter
    def projectname(self, value: str) -> None:
        self._project_name = value

    @projectname.deleter
    def projectname(self) -> str:
        tmp = self._project_name
        self._project_name = None

        return tmp