import project_challanges
import re

from inspect import getmembers, isfunction

challenge_list = [o for o in getmembers(project_challanges) if isfunction(o[1])]
challenge_list = filter(lambda x: re.search('challenge_\d*', x[0]), challenge_list)

print('Starting Euler Project')

for i, challenge in enumerate(challenge_list):
    print(f'Result for {i+1}: {challenge[1]()}')
