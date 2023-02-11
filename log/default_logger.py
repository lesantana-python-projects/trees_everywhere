from logging import Logger


class LoggerDefault(Logger):

    def __define_log_level(self, kwargs, login_level):
        extra = kwargs.get("extra", {})
        if not extra:
            kwargs.update({"extra": extra})

        logging_default = extra.get("logging_level")
        if not logging_default:
            extra.update({"logging_level": login_level})

    def exception(self, *args, **kwargs):
        self.__define_log_level(kwargs, 'EXCEPTION')
        super(LoggerDefault, self).exception(*args, **kwargs)

    def health(self, *args, **kwargs):
        self.__define_log_level(kwargs, 'HEALTH')
        super(LoggerDefault, self).exception(*args, **kwargs)
