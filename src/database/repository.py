from src.database.repository_user import RepositoryUser


class Repository:
    def __init__(self,
                 repo_user: RepositoryUser):
        self.repo_user: RepositoryUser = repo_user


repo_user_inst: RepositoryUser = RepositoryUser()
repository: Repository = Repository(repo_user=repo_user_inst)
