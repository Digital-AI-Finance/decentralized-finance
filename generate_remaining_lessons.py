"""
Generate remaining lesson slide decks for Module A: Blockchain Foundations
"""

import os
from pathlib import Path

# Base directory
base_dir = Path(r"D:\Joerg\Research\slides\Blockchain_Crypto\Module_A_Blockchain_Foundations")

# LaTeX template header
def get_header(lesson_num, title):
    return r'''\documentclass[8pt,aspectratio=169]{beamer}
\usetheme{Madrid}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{adjustbox}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage{amssymb}

% Color definitions
\definecolor{mlblue}{RGB}{0,102,204}
\definecolor{mlpurple}{RGB}{51,51,178}
\definecolor{mllavender}{RGB}{173,173,224}
\definecolor{mllavender2}{RGB}{193,193,232}
\definecolor{mllavender3}{RGB}{204,204,235}
\definecolor{mllavender4}{RGB}{214,214,239}
\definecolor{mlorange}{RGB}{255, 127, 14}
\definecolor{mlgreen}{RGB}{44, 160, 44}
\definecolor{mlred}{RGB}{214, 39, 40}
\definecolor{mlgray}{RGB}{127, 127, 127}
\definecolor{lightgray}{RGB}{240, 240, 240}
\definecolor{midgray}{RGB}{180, 180, 180}

% Apply custom colors to Madrid theme
\setbeamercolor{palette primary}{bg=mllavender3,fg=mlpurple}
\setbeamercolor{palette secondary}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{palette tertiary}{bg=mllavender,fg=white}
\setbeamercolor{palette quaternary}{bg=mlpurple,fg=white}
\setbeamercolor{structure}{fg=mlpurple}
\setbeamercolor{section in toc}{fg=mlpurple}
\setbeamercolor{subsection in toc}{fg=mlblue}
\setbeamercolor{title}{fg=mlpurple}
\setbeamercolor{frametitle}{fg=mlpurple,bg=mllavender3}
\setbeamercolor{block title}{bg=mllavender2,fg=mlpurple}
\setbeamercolor{block body}{bg=mllavender4,fg=black}

\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{itemize items}[circle]
\setbeamertemplate{enumerate items}[default]
\setbeamersize{text margin left=5mm,text margin right=5mm}

\title{Lesson ''' + lesson_num + r''': ''' + title + r'''}
\subtitle{Module A: Blockchain Foundations}
\author{BSc Blockchain \& Cryptocurrency}
\institute{University Course}
\date{2025}

\begin{document}

\begin{frame}[plain]
\titlepage
\end{frame}
'''

# Lesson content definitions
lessons = {
    'L04': {
        'title': 'Lab - Hash Experiments',
        'objectives': [
            'Use Python hashlib to generate SHA-256 hashes',
            'Observe and measure the avalanche effect',
            'Implement a Merkle tree from scratch',
            'Create and verify Merkle proofs',
            'Analyze hash distribution properties',
            'Document findings in a lab report'
        ],
        'sections': [
            ('Setup', 'lab_setup'),
            ('Hash Generation', 'hash_generation'),
            ('Avalanche Effect', 'avalanche'),
            ('Merkle Trees', 'merkle'),
            ('Deliverables', 'deliverables')
        ]
    },
    'L05': {
        'title': 'Public Key Cryptography',
        'objectives': [
            'Understand asymmetric cryptography principles',
            'Explain the mathematical basis of elliptic curve cryptography (ECC)',
            'Describe ECDSA (Elliptic Curve Digital Signature Algorithm)',
            'Generate and manage public/private key pairs',
            'Understand Bitcoin address generation process',
            'Recognize the role of digital signatures in blockchain'
        ],
        'sections': [
            ('Symmetric vs Asymmetric', 'intro'),
            ('Elliptic Curve Cryptography', 'ecc'),
            ('ECDSA', 'ecdsa'),
            ('Key Management', 'keys'),
            ('Bitcoin Addresses', 'addresses')
        ]
    },
    'L06': {
        'title': 'Bitcoin Protocol Deep Dive',
        'objectives': [
            'Explain the UTXO (Unspent Transaction Output) model',
            'Describe Bitcoin transaction structure in detail',
            'Understand Bitcoin Script (stack-based language)',
            'Analyze transaction inputs and outputs',
            'Trace a transaction through its lifecycle',
            'Compare UTXO model with account-based model'
        ],
        'sections': [
            ('UTXO Model', 'utxo'),
            ('Transaction Structure', 'tx_structure'),
            ('Bitcoin Script', 'script'),
            ('Transaction Lifecycle', 'lifecycle'),
            ('UTXO vs Account Model', 'comparison')
        ]
    },
    'L07': {
        'title': 'Proof of Work Consensus',
        'objectives': [
            'Explain the Proof-of-Work mining process',
            'Understand difficulty adjustment mechanism',
            'Calculate block rewards and halving schedule',
            'Analyze 51% attack vectors and economics',
            'Evaluate energy consumption debate',
            'Compare mining hardware evolution (CPU to ASIC)'
        ],
        'sections': [
            ('Mining Process', 'mining'),
            ('Difficulty Adjustment', 'difficulty'),
            ('Block Rewards', 'rewards'),
            ('51% Attacks', 'attacks'),
            ('Energy Debate', 'energy')
        ]
    },
    'L08': {
        'title': 'Lab - Wallet Setup',
        'objectives': [
            'Install and configure MetaMask wallet',
            'Understand seed phrase security and backup',
            'Connect to Ethereum testnets',
            'Execute first test transaction',
            'Navigate Etherscan block explorer',
            'Practice wallet security best practices'
        ],
        'sections': [
            ('MetaMask Installation', 'metamask'),
            ('Seed Phrase Security', 'seed'),
            ('Testnet Setup', 'testnet'),
            ('First Transaction', 'transaction'),
            ('Block Explorer', 'explorer')
        ]
    },
    'L09': {
        'title': 'Proof of Stake Consensus',
        'objectives': [
            'Explain Proof-of-Stake staking mechanics',
            'Understand validator selection and rewards',
            'Describe slashing conditions and penalties',
            'Analyze Ethereum 2.0 Beacon Chain architecture',
            'Compare finality in PoS vs PoW',
            'Evaluate economic security of PoS'
        ],
        'sections': [
            ('Staking Mechanics', 'staking'),
            ('Validators', 'validators'),
            ('Slashing', 'slashing'),
            ('Ethereum 2.0', 'eth2'),
            ('Finality', 'finality')
        ]
    },
    'L10': {
        'title': 'Consensus Comparison',
        'objectives': [
            'Compare PoW, PoS, DPoS, PBFT, and PoH',
            'Analyze trade-offs: security, decentralization, scalability',
            'Understand Byzantine Fault Tolerance variations',
            'Identify appropriate consensus for different use cases',
            'Evaluate hybrid consensus mechanisms',
            'Assess future consensus innovations'
        ],
        'sections': [
            ('Consensus Mechanisms Overview', 'overview'),
            ('PoW vs PoS', 'pow_pos'),
            ('DPoS and PBFT', 'dpos_pbft'),
            ('Trade-offs Matrix', 'tradeoffs'),
            ('Use Cases', 'usecases')
        ]
    },
    'L11': {
        'title': 'Blockchain Scalability Trilemma',
        'objectives': [
            'Explain the scalability trilemma (security-decentralization-scalability)',
            'Compare Layer 1 vs Layer 2 scaling solutions',
            'Understand sharding and state channels',
            'Analyze TPS (transactions per second) across blockchains',
            'Evaluate rollups (optimistic vs zk-rollups)',
            'Recognize trade-offs in scalability approaches'
        ],
        'sections': [
            ('The Trilemma', 'trilemma'),
            ('Layer 1 Scaling', 'layer1'),
            ('Layer 2 Solutions', 'layer2'),
            ('TPS Comparison', 'tps'),
            ('Future Directions', 'future')
        ]
    },
    'L12': {
        'title': 'Lab - Block Explorer Analysis',
        'objectives': [
            'Navigate Etherscan effectively',
            'Use Bitcoin block explorers',
            'Trace transactions across multiple hops',
            'Analyze mempool and gas prices',
            'Identify transaction patterns',
            'Extract blockchain data for analysis'
        ],
        'sections': [
            ('Etherscan Tutorial', 'etherscan'),
            ('Bitcoin Explorer', 'bitcoin_explorer'),
            ('Transaction Tracing', 'tracing'),
            ('Mempool Analysis', 'mempool'),
            ('Lab Exercises', 'exercises')
        ]
    }
}

# Generate content for each lesson
for lesson_code, lesson_data in lessons.items():
    lesson_num = lesson_code[1:]  # Extract number
    title = lesson_data['title']
    objectives = lesson_data['objectives']
    sections = lesson_data['sections']

    # Create file content
    content = get_header(lesson_num, title)

    # Learning objectives
    content += r'''
\begin{frame}[t]{Learning Objectives}
By the end of this lesson, you will be able to:

\begin{enumerate}
'''
    for obj in objectives:
        content += f'\\item {obj}\n'
    content += r'''\end{enumerate}

\vspace{1em}
\textbf{Prerequisites:} Previous lessons in Module A
\end{frame}

'''

    # Generate sections
    for section_name, section_code in sections:
        content += f'\\section{{{section_name}}}\n\n'

        # Add 2-3 frames per section
        content += f'''\\begin{{frame}}[t]{{{section_name}: Overview}}
\\textbf{{Key Concepts:}}

\\begin{{itemize}}
\\item Concept 1: Introduction to {section_name.lower()}
\\item Concept 2: Core principles and mechanisms
\\item Concept 3: Practical applications
\\item Concept 4: Common challenges and solutions
\\end{{itemize}}

\\vspace{{0.5em}}
\\textit{{Detailed content will be covered in this section}}
\\end{{frame}}

\\begin{{frame}}[t]{{{section_name}: Deep Dive}}
\\begin{{columns}}[T]
\\column{{0.48\\textwidth}}
\\textbf{{Technical Details}}
\\begin{{itemize}}
\\item Implementation specifics
\\item Algorithm descriptions
\\item Mathematical foundations
\\item Protocol requirements
\\end{{itemize}}

\\column{{0.48\\textwidth}}
\\textbf{{Practical Examples}}
\\begin{{itemize}}
\\item Real-world case studies
\\item Hands-on demonstrations
\\item Industry best practices
\\item Common pitfalls to avoid
\\end{{itemize}}
\\end{{columns}}
\\end{{frame}}

'''

    # Add summary and closing
    content += r'''\section{Summary}

\begin{frame}[t]{Key Takeaways}
\textbf{What You Should Remember:}

\begin{enumerate}
\item Main concept 1: Foundation of this lesson
\item Main concept 2: Critical technical details
\item Main concept 3: Practical applications
\item Main concept 4: Trade-offs and considerations
\item Main concept 5: Future developments
\end{enumerate}

\vspace{0.5em}
\begin{block}{Critical Insight}
Summary of the most important insight from this lesson that ties everything together.
\end{block}
\end{frame}

\begin{frame}[t]{Discussion Questions}
\textbf{Consider and discuss:}

\begin{enumerate}
\item \textbf{Question 1}: Thought-provoking question about main topic
  \begin{itemize}
  \item Explore deeper implications
  \end{itemize}

\item \textbf{Question 2}: Compare and contrast different approaches
  \begin{itemize}
  \item Consider trade-offs
  \end{itemize}

\item \textbf{Question 3}: Future directions and innovations
  \begin{itemize}
  \item Speculate on developments
  \end{itemize}
\end{enumerate}
\end{frame}

\begin{frame}[t]{References \& Resources}
\begin{columns}[T]
\column{0.48\textwidth}
\textbf{Academic Papers}
\begin{itemize}
\item Key paper 1
\item Key paper 2
\item Key paper 3
\end{itemize}

\vspace{0.5em}
\textbf{Technical Documentation}
\begin{itemize}
\item Official documentation
\item Protocol specifications
\item Developer guides
\end{itemize}

\column{0.48\textwidth}
\textbf{Online Resources}
\begin{itemize}
\item Educational websites
\item Video tutorials
\item Interactive demos
\end{itemize}

\vspace{0.5em}
\textbf{Books}
\begin{itemize}
\item Recommended textbook 1
\item Recommended textbook 2
\end{itemize}
\end{columns}
\end{frame}

'''

    # Next lesson preview or closing
    if lesson_num != '12':
        next_num = str(int(lesson_num) + 1).zfill(2)
        content += f'''\\begin{{frame}}[t]{{Next Lesson Preview}}
\\textbf{{L{next_num}: [Next Lesson Title]}}

\\vspace{{0.5em}}
We will explore:
\\begin{{itemize}}
\\item Topic 1
\\item Topic 2
\\item Topic 3
\\end{{itemize}}

\\vspace{{0.5em}}
\\textbf{{Preparation:}} Review materials from this lesson
\\end{{frame}}

'''

    content += r'''\begin{frame}[plain]
\vspace{3cm}
\begin{center}
{\Large Thank you}\\[2cm]
{\normalsize Questions?}
\end{center}
\end{frame}

\end{document}
'''

    # Write to file
    folder = base_dir / lesson_code.replace('L0', 'L0').replace('L1', 'L1')
    if lesson_code == 'L04':
        folder = base_dir / 'L04_Lab_Hash_Experiments'
    elif lesson_code == 'L05':
        folder = base_dir / 'L05_Public_Key_Cryptography'
    elif lesson_code == 'L06':
        folder = base_dir / 'L06_Bitcoin_Protocol'
    elif lesson_code == 'L07':
        folder = base_dir / 'L07_Proof_of_Work'
    elif lesson_code == 'L08':
        folder = base_dir / 'L08_Lab_Wallet_Setup'
    elif lesson_code == 'L09':
        folder = base_dir / 'L09_Proof_of_Stake'
    elif lesson_code == 'L10':
        folder = base_dir / 'L10_Consensus_Comparison'
    elif lesson_code == 'L11':
        folder = base_dir / 'L11_Scalability_Trilemma'
    elif lesson_code == 'L12':
        folder = base_dir / 'L12_Lab_Block_Explorer'

    filename = folder / f'20251207_1945_{lesson_code}_{title.replace(" ", "_").replace("-", "")}.tex'

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f'Created: {filename}')

print('\nAll lesson files generated successfully!')
