#estruturando dados com pandas

import pandas

mydataset = {
'': ["    --345     ","-----------567656           ", "--null    " , "-1-", "79                            ", " null               "]

}
myvar = pandas.DataFrame(mydataset)
print(myvar)
