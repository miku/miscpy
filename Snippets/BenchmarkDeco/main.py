from timeit import default_timer
import functools

class Timer(object):
    """
    A timer as a context manager, slight visual language.
    """
    def __init__(self):
        # measures wall clock time, not CPU time!
        # On Unix systems, it corresponds to time.time
        # On Windows systems, it corresponds to time.clock
        self.timer = default_timer

    def __enter__(self):
        self.start = self.timer()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.end = self.timer()
        self.elapsed_s = self.end - self.start
        self.elapsed_ms = self.elapsed_s * 1000


def timed(f):
    """
    A @timed decorator.
    """
    @functools.wraps(f)
    def _timed(*args, **kwargs):
        """
        Benchmark decorator.
        """
        with Timer() as timer:
            result = f(*args, **kwargs)
        klass = args[0].__class__.__name__
        fun = f.__name__

        msg = "[%s.%s] %0.5f" % (klass, fun, timer.elapsed_s)
        print(msg)
        return result

    return 