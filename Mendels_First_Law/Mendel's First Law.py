
def firstlaw (k, m, n):
    tot = k + m + n

    k_tot = k/tot
    kk = k_tot * (k-1)/(tot-1)
    km = k_tot * (m/(tot-1))
    kn = k_tot * (n/(tot-1))

    m_tot = m/tot
    mk = m_tot * (k/(tot-1))
    mm = m_tot * (m-1)/(tot-1) * 0.75
    mn = m_tot * (n/(tot-1)) * 0.5

    n_tot = n/tot
    nk = n_tot * (k/(tot-1))
    nm = n_tot * (m/(tot-1)) * 0.5
    nn = n_tot * (n-1)/(tot-1)* 0

    # Create an output file with counts
    with open("mendels_first_law_ans.txt", 'w') as file:
        # Format the print of the pairs according to instructions
        file.write(str(kk + km + kn + mk + mm + mn + nk + nm + nn))

k, m, n = open("rosalind_iprb.txt").read().split(" ")

k, m, n = int(k), int(m), int(n)

firstlaw(k, m , n)
