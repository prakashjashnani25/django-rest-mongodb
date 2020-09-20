class DBRouter:
    routes = ['RestMongo']
    
    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.routes:
            return "mongo_db"
        return None
    
    def db_for_write(self,model, **hints):
        if model._meta.app_label in self.routes:
            return "mongo_db"