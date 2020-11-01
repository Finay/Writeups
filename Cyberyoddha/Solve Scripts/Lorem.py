given = 'Lorem ipsum dolorc sit amet, consectetury adipiscing celit, sed dot eiusmod tempor incifdidunt ut labore et dolore magna aliqual. Ut enim ad minima veniam, quist nostrud exercitation ullamcoi laboris nisin ut aliquip ex eai commodos consequat. Duis caute irure dolor in reprehenderit in voluptate velit oesse cillum dolore eu fugiat nulla pariatur. Excepteur osint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim lid est laborum.'
real = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

offset = 0

for i in range(len(given)):
    #print(given[i], real[i-offset])
    if given[i] != real[i-offset]:
        print(given[i], end="")
        offset += 1
