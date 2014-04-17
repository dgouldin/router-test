class TestRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'foo':
            return 'other'
        else:
            return 'default'

    db_for_write = db_for_read

    def allow_syncdb(self, db, model):
        should_sync = (model._meta.app_label == 'foo') == (db == 'other')
        print 'SYNCDB: {0}, {1}: {2}'.format(db, model, should_sync)
        return should_sync
