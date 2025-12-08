# Quiz 2: Ethereum Basics
## BSc Blockchain, Crypto Economy & NFTs

**Lectures Covered**: L09-L16 (Ethereum Introduction through Smart Contract Development)
**Duration**: 30 minutes
**Total Points**: 100 points
**Question Types**: 6 multiple choice (8 pts each), 4 short answer (13 pts each)

---

## Multiple Choice Questions (48 points total)

### Question 1 (8 points)
**Topic**: Ethereum Architecture

What is the primary difference between Bitcoin and Ethereum?

A) Bitcoin is decentralized while Ethereum is centralized
B) Bitcoin uses proof-of-work while Ethereum has always used proof-of-stake
C) Ethereum is a programmable blockchain with smart contract functionality, while Bitcoin is primarily a payment system
D) Ethereum transactions are faster because it uses different cryptography

**Correct Answer**: C

**Explanation**: Ethereum's key innovation is its Turing-complete virtual machine (EVM) that enables smart contracts - programmable, self-executing code. Bitcoin primarily focuses on peer-to-peer payments. Note: Ethereum transitioned to proof-of-stake in 2022 (The Merge), but both networks previously used proof-of-work.

---

### Question 2 (8 points)
**Topic**: Smart Contracts

What is a smart contract in the context of Ethereum?

A) A legal contract stored on the blockchain
B) Self-executing code deployed on the blockchain that runs when predetermined conditions are met
C) An encrypted agreement between two parties
D) A contract that can modify itself automatically

**Correct Answer**: B

**Explanation**: Smart contracts are programs stored on the blockchain that automatically execute when specific conditions are met. They are not legal contracts per se, though they can encode agreement terms. Once deployed, their code is immutable.

---

### Question 3 (8 points)
**Topic**: Ethereum Gas

What is the purpose of "gas" in the Ethereum network?

A) To encrypt transaction data
B) To measure and limit computational work, preventing infinite loops and spam while compensating validators
C) To determine transaction priority only
D) To convert ETH into fiat currency

**Correct Answer**: B

**Explanation**: Gas serves multiple purposes: (1) measures computational complexity of operations, (2) prevents infinite loops/DoS attacks by limiting execution, (3) compensates validators for computation, and (4) creates a fee market for block space.

---

### Question 4 (8 points)
**Topic**: Solidity Basics

In Solidity, what visibility modifier makes a function callable from outside the contract?

A) internal
B) private
C) public
D) protected

**Correct Answer**: C

**Explanation**: Public functions can be called both internally (within the contract) and externally (from outside). Private functions are only callable within the defining contract, and internal functions are callable within the contract and derived contracts. Solidity does not have a "protected" modifier.

---

### Question 5 (8 points)
**Topic**: Ethereum Accounts

What is the key difference between an Externally Owned Account (EOA) and a Contract Account in Ethereum?

A) EOAs can hold ETH, contract accounts cannot
B) EOAs are controlled by private keys, while contract accounts are controlled by code
C) Contract accounts can initiate transactions, EOAs cannot
D) EOAs are free to create, contract accounts cost gas

**Correct Answer**: B

**Explanation**: EOAs are controlled by private keys and can initiate transactions. Contract accounts are controlled by their code and can only execute when triggered by a transaction from an EOA or another contract. Both can hold ETH.

---

### Question 6 (8 points)
**Topic**: EVM and State

What does it mean that the Ethereum Virtual Machine (EVM) is "Turing-complete"?

A) It can run indefinitely without stopping
B) It can compute any computable function given enough resources
C) It executes code faster than other virtual machines
D) It can verify its own correctness

**Correct Answer**: B

**Explanation**: Turing-completeness means the EVM can theoretically compute any function that is computable, given sufficient time and memory. This enables complex logic but requires gas limits to prevent infinite execution. Option A is incorrect because gas limits prevent indefinite execution.

---

## Short Answer Questions (52 points total)

### Question 7 (13 points)
**Topic**: Gas Mechanism

Explain how gas fees work in Ethereum. In your answer, describe gas limit, gas price, and what happens if a transaction runs out of gas.

**Model Answer** (for grading reference):

Gas fees in Ethereum work as follows:

**Gas Limit**: The maximum amount of gas units a user is willing to spend on a transaction. Different operations consume different amounts of gas (e.g., addition costs 3 gas, SSTORE costs 20,000+ gas).

**Gas Price**: The amount of ETH (in gwei) a user is willing to pay per unit of gas. After EIP-1559, this includes a base fee (burned) and optional priority fee (tip to validators).

**Transaction Cost**: Total fee = Gas Used × Gas Price (or Base Fee + Priority Fee)

**Running Out of Gas**: If a transaction's execution consumes all allocated gas before completing, the transaction reverts (all state changes are undone), but the gas consumed is still paid to validators. This prevents infinite loops and ensures validators are compensated for computational work performed.

**Example**: If gas limit = 50,000 units and gas price = 20 gwei, maximum cost = 0.001 ETH. If execution only uses 30,000 gas, user pays 0.0006 ETH and receives refund for unused 20,000 gas.

**Grading Criteria**:
- 13 points: Explains gas limit, gas price, calculation, and out-of-gas behavior clearly
- 9-12 points: Covers main concepts but missing some details
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

### Question 8 (13 points)
**Topic**: Smart Contract Security

What is a "reentrancy attack" in smart contracts? Describe how it works and mention one way to prevent it.

**Model Answer** (for grading reference):

A reentrancy attack occurs when a malicious contract calls back into the vulnerable contract before the first invocation completes, potentially draining funds or manipulating state.

**How it works**:
1. Victim contract has a withdrawal function that sends ETH before updating the user's balance
2. Attacker contract calls the withdrawal function
3. When victim contract sends ETH, it triggers attacker's fallback/receive function
4. Attacker's fallback function calls the withdrawal function again
5. Since the balance hasn't been updated yet, the victim contract sends ETH again
6. This repeats until the victim contract is drained

**Famous Example**: The DAO hack (2016) exploited reentrancy to steal ~60 million worth of ETH.

**Prevention Methods**:
1. **Checks-Effects-Interactions Pattern**: Update state variables before external calls
2. **Reentrancy Guards**: Use a mutex lock to prevent reentrant calls (e.g., OpenZeppelin's ReentrancyGuard)
3. **Use transfer() or send()**: Instead of call.value() (though this has limitations)

**Grading Criteria**:
- 13 points: Clear explanation of attack mechanism + specific prevention method
- 9-12 points: Good explanation but less detailed
- 6-8 points: Basic understanding but lacks precision
- 3-5 points: Vague or incomplete
- 0-2 points: Incorrect or no meaningful answer

---

### Question 9 (13 points)
**Topic**: Solidity Data Types and Storage

Explain the difference between "storage," "memory," and "calldata" in Solidity. When would you use each?

**Model Answer** (for grading reference):

Solidity has three data location keywords that determine where variables are stored:

**Storage**:
- Permanent storage on the blockchain (state variables)
- Persists between function calls and transactions
- Most expensive in terms of gas
- Default location for state variables
- Example: Contract balance mappings, owner addresses

**Memory**:
- Temporary storage that exists only during function execution
- Erased between external function calls
- Less expensive than storage
- Used for function parameters and local variables
- Example: Temporary arrays, function return values

**Calldata**:
- Non-modifiable, temporary location for function parameters
- Only available for external function parameters
- Cheapest option for passing data
- Read-only (cannot be modified)
- Example: External function parameters, especially arrays or structs

**Usage Guidelines**:
- Use storage for state variables that need persistence
- Use memory for temporary variables in functions
- Use calldata for external function parameters (especially arrays/strings) to save gas

**Example**:
```solidity
contract Example {
    uint[] public numbers; // storage

    function processData(uint[] calldata input) external {
        uint[] memory temp = new uint[](input.length); // memory
        // Process data...
    }
}
```

**Grading Criteria**:
- 13 points: Clear explanation of all three + usage examples
- 9-12 points: Explains all three but less comprehensive
- 6-8 points: Covers storage and memory well but weak on calldata
- 3-5 points: Vague or incomplete understanding
- 0-2 points: Incorrect or no meaningful answer

---

### Question 10 (13 points)
**Topic**: Ethereum State Transition

Describe what happens when a user sends a transaction to call a smart contract function on Ethereum. Include the role of validators, gas, and state changes.

**Model Answer** (for grading reference):

When a user sends a transaction to call a smart contract function:

**1. Transaction Creation**:
- User creates a transaction with: recipient (contract address), function call data, gas limit, and gas price
- User signs transaction with private key
- Transaction is broadcast to Ethereum network

**2. Mempool**:
- Transaction enters the mempool (pending transactions)
- Validators see the transaction and consider including it based on gas price/priority fee

**3. Block Inclusion**:
- A validator selects transactions from mempool to include in the next block
- Transactions with higher priority fees are typically chosen first
- Validator orders transactions within the block

**4. Execution**:
- EVM executes the contract code with the transaction's parameters
- Each operation consumes gas
- State changes are applied (e.g., variable updates, transfers)
- Events may be emitted

**5. State Transition**:
- If execution succeeds: state changes are committed, gas fee is paid
- If execution fails (error or out of gas): state reverts, but gas consumed is still paid
- New state root is calculated using Merkle Patricia tree

**6. Block Finalization**:
- Validator proposes the block with included transactions
- Other validators attest to block validity
- Block becomes part of the canonical chain
- Transaction reaches finality after sufficient confirmations/attestations

**Grading Criteria**:
- 13 points: Comprehensive flow covering transaction creation through finalization
- 9-12 points: Covers main steps but missing some details
- 6-8 points: Basic understanding of process
- 3-5 points: Incomplete or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

## Answer Key Summary

| Question | Type | Answer | Points |
|----------|------|--------|--------|
| Q1 | MC | C | 8 |
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

**Lectures L09-L16**:
- Ethereum architecture and philosophy
- Smart contracts fundamentals
- Ethereum accounts (EOA vs Contract)
- Gas mechanism and transaction fees
- Ethereum Virtual Machine (EVM)
- Solidity basics (data types, visibility, functions)
- Storage vs memory vs calldata
- Smart contract security (reentrancy, overflow)
- Development tools (Remix, Hardhat, Foundry)
- Testing smart contracts
- Deployment process
- State transitions and block production

---

## Study Recommendations

- Review lecture slides L09-L16
- Understand the gas mechanism and how fees are calculated
- Practice writing basic Solidity contracts
- Study smart contract security vulnerabilities (especially reentrancy)
- Know the difference between storage, memory, and calldata
- Understand Ethereum's account model and state transitions
- Review EVM basics and Turing-completeness
- Practice deploying contracts on testnets
