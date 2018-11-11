import pickle
from sklearn.ensemble import RandomForestClassifier

class MacOSFile(object):

    def __init__(self, f):
        self.f = f

    def __getattr__(self, item):
        return getattr(self.f, item)

    def read(self, n):
        # print("reading total_bytes=%s" % n, flush=True)
        if n >= (1 << 31):
            buffer = bytearray(n)
            idx = 0
            while idx < n:
                batch_size = min(n - idx, 1 << 31 - 1)
                # print("reading bytes [%s,%s)..." % (idx, idx + batch_size), end="", flush=True)
                buffer[idx:idx + batch_size] = self.f.read(batch_size)
                # print("done.", flush=True)
                idx += batch_size
            return buffer
        return self.f.read(n)

# def pickle_dump(obj, file_path):
#     with open('/Users/atg/Desktop/astroDSserv/main/model_fitted', "wb") as f:
#         return pickle.dump(obj, MacOSFile(f), protocol=pickle.HIGHEST_PROTOCOL)


def pickle_load(file_path):
    with open(file_path, "rb") as f:
        return pickle.load(MacOSFile(f))

MODEL = pickle_load('/Users/atg/Desktop/astroDSserv/main/model_fitted')

#bin_data = open('/Users/atg/Desktop/astroDSserv/main/model_fitted', 'rb')
#MODEL = pickle.loads(MacOSFile(bin_data.read()))
#bin_data.close()
