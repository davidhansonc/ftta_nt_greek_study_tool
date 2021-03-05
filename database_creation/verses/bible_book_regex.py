nt_regex = {
    'Matthew': '.*(M[a-z]*t[a-z]*)[\s\.](\d+):(\d+)[\s]*(.*)',
    'Mark': '(M[a-z]*k[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Luke': '(L[a-z]*k[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'John': '(^J[a-z]*n[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Acts': '(A[a-z]*c[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Romans': '(R[a-z]*m[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'First Corinthians': '(1C[a-z]*o[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Second Corinthians': '(2C[a-z]*o[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Galatians': '(G[a-z]*a[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Ephesians': '(E[a-z]*p[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Philippians': '(P[a-ln-z]+)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Colossians': '(C[a-z]*o[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'First Thessalonians': '(1Th[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Second Thessalonians': '(2Th[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'First Timothy': '(1Ti[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Second Timothy': '(2Ti[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Titus': '(T[a-z]*t[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Philemon': '(P[a-z]*m[a-z]*)[\s\.](\d*):?(\d+)[\s]*(.+)',
    'Hebrews': '(H[a-z]*e[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'James': '(J[a-z]*a[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'First Peter': '(1P[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Second Peter': '(2P[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'First John': '(1J[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
    'Second John': '(2J[a-z]*)[\s\.](\d*):?(\d+)[\s]*(.+)',
    'Third John': '(3J[a-z]*)[\s\.](\d*):?(\d+)[\s]*(.+)',
    'Jude': '(J[a-z]*d[a-z]*)[\s\.](\d*):?(\d+)[\s]*(.+)',
    'Revelation': '(R[a-z]*v[a-z]*)[\s\.](\d+):(\d+)[\s]*(.+)',
}