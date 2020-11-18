from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
session = WolframLanguageSession()
print(session.evaluate(wlexpr('Select[Range[5],PrimeQ]')))
