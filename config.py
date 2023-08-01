import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "20244111"))
    API_HASH = os.environ.get("API_HASH", "b76d27da2a4220fe109fe9ef0e866530")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6118269542:AAFmgpviq2esTYYpdaGTc3Ch1RQntbcOAcs")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5572938538")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://MohanishX1:Jobijobi@1@cluster0.tubnaa7.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQA7ejnvkmHAL91BlNLjKZfeeHMpBJAsnCwOOWwnhqk3CcE0lsDlPX6-gYiICYNRua7k8Q3Yjb3Ttcqyb7vg-G-8SnMLEZSRFUs4nbVen0kHukLRiQaH8emD0oFFy-McYWm0lIeUg07sC4AG2JPIiqua0gF2Qjyk6XQ_Jn2y0MNnhCmxs8v2HXEWLoBdDl-mjaWu3FZs4nzVQNetMsaL7rYcnBfDii8kniHb1vVht-8LVVmkrCSp4Nvz2kQoe6pcCd_vQr-fR3K-VrB2XqFgzPZox4tcFw3FipMr2CxC4k6pVL4mgctP4YQGadSMq1xaFZ4GSquwgzrwoaHEwk9NCeVHAAAAAUwsSyoA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001237016020"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "mohanish")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
