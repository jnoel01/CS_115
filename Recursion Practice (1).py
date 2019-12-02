#Jessica Noel
#9/11/19
#CS115 B/C
#"I pledge my honor that I have abided by the Stevens Honor System."

def dotProduct(L,K):
    '''Produce the dotproduct of the of lists and L and K when ran'''
    if []==L and []==K:
        return 0
    else:
      return L[0]*K[0] + dotProduct(L[1:], K[1:])


def expand(S):
    '''Expand list S into a list of individual chracters that are contained within S'''
    L=[]
    if ""==S:
        return []
    else:
        L += S[0]
        L += expand(S[1:])
    return L


def deepMember(e,L):
    '''deepMember will find if e is present within L, if so return True if false return False'''
    if L==[]:
        return False

    elif L[0]==e:
        return True

    elif isinstance(L[0], list):
        if L[0][0] == e:
            return True
        else:
            return deepMember(e, L[0][1:]+L[1:])
    else:
        return deepMember(e,L[1:])


def removeAll(e,L):
    '''if e is present in L them remove e'''
    K=[]
    if []==L:
        return K
    if e==L[0]:
        return removeAll(e,L[1:])
    elif isinstance(L[0], list):
        if L[0][0] == e:
            return removeAll(e, L[0][1:]+L[1:])
        else:
            K.append(L[0])
            return removeAll(e, L[0][1:]+L[1:])
    else:
        K.append(L[0])
        K+=removeAll(e,L[1:])
    return K


def deepReverse(L):
    '''deepReverse will reverse a given list'''
    K=[]
    if []==L:
        return K
    else:
        K+=deepReverse(L[1:])
        K.append(L[0])
    return K
