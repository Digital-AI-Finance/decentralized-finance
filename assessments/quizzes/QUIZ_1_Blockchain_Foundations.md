# Quiz 1: Blockchain Foundations
## BSc Blockchain, Crypto Economy & NFTs

**Lectures Covered**: L01-L08 (Introduction through Consensus Mechanisms)
**Duration**: 30 minutes
**Total Points**: 100 points
**Question Types**: 6 multiple choice (8 pts each), 4 short answer (13 pts each)

---

## Multiple Choice Questions (48 points total)

### Question 1 (8 points)
**Topic**: Blockchain Basics

What is the primary purpose of a hash function in blockchain technology?

A) To encrypt transaction data for privacy
B) To create a unique, fixed-size fingerprint of data that is deterministic and collision-resistant
C) To compress large files into smaller sizes
D) To verify user identities on the network

**Correct Answer**: B

**Explanation**: Hash functions create deterministic, unique fingerprints (hashes) of data. They are collision-resistant (hard to find two inputs with the same hash) and one-way (cannot reverse engineer input from hash). They are NOT encryption mechanisms.

---

### Question 2 (8 points)
**Topic**: Cryptographic Foundations

In public-key cryptography used by Bitcoin and Ethereum, which statement is TRUE?

A) The private key is derived from the public key
B) The public key can be shared openly and is used to verify signatures
C) Both private and public keys must be kept secret
D) The private key is longer than the public key

**Correct Answer**: B

**Explanation**: Public keys are derived from private keys (not vice versa). Public keys can be shared openly and are used to verify signatures created with the corresponding private key. Only the private key must be kept secret.

---

### Question 3 (8 points)
**Topic**: Distributed Systems

What problem does Byzantine Fault Tolerance (BFT) address in distributed systems?

A) Network latency issues
B) The presence of malicious or faulty nodes that may send incorrect information
C) Storage capacity limitations
D) Transaction speed optimization

**Correct Answer**: B

**Explanation**: Byzantine Fault Tolerance addresses the challenge of reaching consensus in a distributed system when some nodes may be malicious or faulty. The Byzantine Generals Problem illustrates this coordination challenge in adversarial environments.

---

### Question 4 (8 points)
**Topic**: Bitcoin Basics

What is the primary role of "mining" in the Bitcoin network?

A) To create new user accounts
B) To encrypt transactions for security
C) To validate transactions and secure the network through proof-of-work while earning rewards
D) To store the complete blockchain history

**Correct Answer**: C

**Explanation**: Mining serves two purposes: (1) validating and bundling transactions into blocks, and (2) securing the network through computational proof-of-work. Miners are rewarded with newly created bitcoins (block subsidy) and transaction fees.

---

### Question 5 (8 points)
**Topic**: Consensus Mechanisms

Which consensus mechanism requires participants to "stake" cryptocurrency as collateral?

A) Proof of Work (PoW)
B) Proof of Stake (PoS)
C) Proof of Authority (PoA)
D) Delegated Proof of Work

**Correct Answer**: B

**Explanation**: Proof of Stake requires validators to lock up (stake) cryptocurrency as collateral. Validators are selected to create blocks based on their stake amount. If they act maliciously, their stake can be "slashed" (confiscated).

---

### Question 6 (8 points)
**Topic**: Merkle Trees

What advantage does a Merkle tree provide for blockchain data structures?

A) It encrypts all transaction data
B) It allows efficient verification of specific transactions without downloading the entire block
C) It compresses the blockchain to save storage space
D) It speeds up transaction processing times

**Correct Answer**: B

**Explanation**: Merkle trees allow for efficient verification of whether a specific transaction is included in a block using only the Merkle root and a small proof (Merkle path). This enables "light clients" to verify transactions without storing the entire blockchain.

---

## Short Answer Questions (52 points total)

### Question 7 (13 points)
**Topic**: Blockchain Immutability

Explain why blockchains are considered "immutable." In your answer, describe the role of cryptographic hashing and how blocks are linked together.

**Model Answer** (for grading reference):

Blockchains are considered immutable because each block contains a cryptographic hash of the previous block, creating a chain. If someone attempts to alter data in a past block, the hash of that block changes, which invalidates all subsequent blocks since their "previous block hash" values would no longer match. This would require recalculating all hashes from that point forward. In proof-of-work systems, this recalculation would require redoing all the computational work for those blocks, making it computationally infeasible to alter historical data, especially as the chain grows longer.

**Grading Criteria**:
- 13 points: Explains hash chaining + impact of changing old blocks + computational difficulty
- 9-12 points: Explains hash chaining and impact on subsequent blocks
- 6-8 points: Mentions hash linking but lacks detail on consequences
- 3-5 points: Vague understanding; minimal explanation
- 0-2 points: Incorrect or no meaningful answer

---

### Question 8 (13 points)
**Topic**: Double-Spending Problem

What is the "double-spending problem" in digital currencies, and how does blockchain technology solve it? Provide a specific example.

**Model Answer** (for grading reference):

The double-spending problem occurs when a digital token (e.g., cryptocurrency) could potentially be spent multiple times, since digital information can be copied. For example, Alice could try to send the same 1 BTC to both Bob and Charlie simultaneously.

Blockchain solves this through:
1. Maintaining a global, distributed ledger that records all transactions
2. Requiring network consensus on transaction ordering
3. Only accepting the first valid transaction (e.g., Alice -> Bob) and rejecting subsequent attempts to spend the same output (Alice -> Charlie would be invalid)
4. Making it computationally infeasible to rewrite history due to proof-of-work or stake-based consensus

**Grading Criteria**:
- 13 points: Clear definition + specific example + comprehensive solution explanation
- 9-12 points: Good definition and solution explanation
- 6-8 points: Basic understanding but lacks detail or example
- 3-5 points: Vague or incomplete understanding
- 0-2 points: Incorrect or no meaningful answer

---

### Question 9 (13 points)
**Topic**: Proof of Work vs Proof of Stake

Compare Proof of Work (PoW) and Proof of Stake (PoS) consensus mechanisms. Identify at least two advantages and one disadvantage of each.

**Model Answer** (for grading reference):

**Proof of Work (PoW)**:
Advantages:
- Proven security track record (Bitcoin since 2009)
- High attack cost (requires massive computational power)
- Permissionless participation (anyone with hardware can mine)

Disadvantages:
- High energy consumption (environmental concerns)
- Centralization risk through mining pools and specialized hardware (ASICs)
- Slower transaction finality

**Proof of Stake (PoS)**:
Advantages:
- Energy efficient (no computational puzzles)
- Lower barrier to participation (no expensive hardware)
- Faster transaction finality
- Economic penalties for misbehavior (slashing)

Disadvantages:
- Less proven at scale historically (though Ethereum's transition is changing this)
- Potential "rich get richer" dynamic (more stake = more rewards)
- "Nothing at stake" problem (theoretical, largely mitigated)

**Grading Criteria**:
- 13 points: Identifies 2+ advantages and 1+ disadvantage for BOTH with clear explanations
- 9-12 points: Identifies advantages/disadvantages for both but less comprehensive
- 6-8 points: Covers one mechanism well or both superficially
- 3-5 points: Incomplete or partially incorrect comparison
- 0-2 points: Incorrect or no meaningful answer

---

### Question 10 (13 points)
**Topic**: Blockchain Trilemma

Explain the "blockchain trilemma" and why it represents a fundamental challenge in blockchain design. Give one example of how a blockchain system makes trade-offs among these three properties.

**Model Answer** (for grading reference):

The blockchain trilemma, proposed by Vitalik Buterin, states that blockchain systems can typically only optimize for two of three properties simultaneously:

1. **Decentralization**: Many independent nodes participate in consensus
2. **Security**: Resistance to attacks and fault tolerance
3. **Scalability**: High transaction throughput and low latency

The trilemma represents a fundamental challenge because improving one property often requires compromising another:

Example: Bitcoin prioritizes decentralization and security but sacrifices scalability (limited to ~7 transactions per second). In contrast, a permissioned blockchain like Hyperledger Fabric achieves high scalability and security but sacrifices decentralization by limiting validators to known entities.

Layer 2 solutions (Lightning Network, rollups) attempt to work around the trilemma by handling transactions off-chain while inheriting security from the main chain.

**Grading Criteria**:
- 13 points: Clear explanation of all three properties + specific example with trade-offs explained
- 9-12 points: Explains trilemma well but example is weak or missing
- 6-8 points: Basic understanding of concept but lacks depth
- 3-5 points: Vague or incomplete understanding
- 0-2 points: Incorrect or no meaningful answer

---

## Answer Key Summary

| Question | Type | Answer | Points |
|----------|------|--------|--------|
| Q1 | MC | B | 8 |
| Q2 | MC | B | 8 |
| Q3 | MC | B | 8 |
| Q4 | MC | C | 8 |
| Q5 | MC | B | 8 |
| Q6 | MC | B | 8 |
| Q7 | SA | See model answer | 13 |
| Q8 | SA | See model answer | 13 |
| Q9 | SA | See model answer | 13 |
| Q10 | SA | See model answer | 13 |
| **Total** | | | **100** |

---

## Topics Covered

**Lectures L01-L08**:
- Introduction to blockchain technology
- Distributed systems and consensus
- Cryptographic foundations (hashing, digital signatures, public-key cryptography)
- Bitcoin architecture and mechanics
- Mining and proof-of-work
- Consensus mechanisms (PoW, PoS, PoA)
- Blockchain data structures (Merkle trees, chain of blocks)
- Double-spending and Byzantine Fault Tolerance
- Blockchain trilemma
- Security and immutability

---

## Study Recommendations

- Review lecture slides L01-L08
- Understand how cryptographic hashing creates immutability
- Be able to explain proof-of-work and proof-of-stake at a conceptual level
- Know the structure of a block and how Merkle trees work
- Understand the blockchain trilemma and trade-offs
- Study Bitcoin's architecture and transaction flow
- Review consensus mechanism comparisons
