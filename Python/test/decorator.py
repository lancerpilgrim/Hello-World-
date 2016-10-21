#  -*- coding: utf-8 -*-


def parameter_init(*arg):
    def _logger(method):
        def __logger(instance, request, *args, **kwargs):
            print 'Call the function %s().' % method.__name__
            for item in arg:
                setattr(instance, item, request[item])
            print instance.__dict__
            return method(instance, request)
        return __logger
    return _logger


class FilterQuestionView(object):
    def __init__(self):
        self.name = "view"

    def dispatch(self, request, *args, **kwargs):
        logger.info("[FilterQuestionView] enter")
        return super(FilterQuestionView, self).dispatch(request, *args, **kwargs)
    
    @parameter_init("x",
                    "y")
    def post(self, request, *args, **kwargs):
        print "post"
        return self.name

    @parameter_init()
    def parameter_verification(self, request):
        print "parameter_verification"
        # try:
        #     setattr(self, "id", str(request.POST.get("id")))
        #     setattr(self, "submit_key", str(request.POST.get("submit_key")))
        #     setattr(self, "subject", str(request.POST.get("subject")))        
        #     setattr(self, "knownledge_points", str(request.POST.get("knownledge_points")))
        #     setattr(self, "difficulty", int(request.POST.get("difficulty")))
        #     setattr(self, "question_type", int(request.POST.get("question_type")))
        #     setattr(self, "last_question_id", str(request.POST.get("last_question_id", 0)))
        #     setattr(self, "num", int(request.POST.get("num")))
        #     client_ip = get_client_ip(request)
        #     client_ua = get_client_ua(request)
        # except Exception as e:
        #     raise RequestParameterError("请求参数错误")
        
        # logger.info("[FilterQuestionView] request parameter: [client_ip=%s] [client_ua=%s] [id=%s] \
        #     [submit_key=%s] [subject=%s] [knownledge_points=%s] [difficulty=%d] [question_type=%d]\
        #     [last_question_id=%d] [num=%d]" % (client_ip, client_ua, self.id, self.submit_key, self.subject, \
        #         self.knownledge_points, self.difficulty, self.question_type, self.last_question_id, self.num))


if __name__ == "__main__":
    f = FilterQuestionView()
    print f.post({"x": 3, "y": 4})

