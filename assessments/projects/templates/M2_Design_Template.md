# Milestone 2: Contract Design
## BSc Blockchain, Crypto Economy & NFTs

**Due**: Week 6
**Weight**: 10% of project grade
**Format**: Technical design document (PDF) + Solidity interfaces

---

## Submission Information

**Team Name**: ___________________________

**Team Members**:
1. ___________________________
2. ___________________________
3. ___________________________ (if applicable)

**Project Title**: ___________________________

**GitHub Repository**: ___________________________

**Submission Date**: _________________________

---

## 1. Architecture Overview (25%)

### 1.1 System architecture diagram

Include a diagram showing:
- All smart contracts
- Relationships between contracts
- External systems (oracles, IPFS, etc.)
- User interactions

[Insert diagram here - use draw.io, Excalidraw, or similar]

---

### 1.2 Contract descriptions

For each smart contract in your system:

**Contract 1: _________________________**

**Purpose**: ___________________________

**Responsibilities**:
- Responsibility 1: ___________________________
- Responsibility 2: ___________________________
- Responsibility 3: ___________________________

**Interacts with**:
- Contract/System 1: ___________________________ (describe interaction)
- Contract/System 2: ___________________________ (describe interaction)

---

**Contract 2: _________________________**

**Purpose**: ___________________________

**Responsibilities**:
- Responsibility 1: ___________________________
- Responsibility 2: ___________________________

**Interacts with**:
- Contract/System 1: ___________________________ (describe interaction)

---

(Add more contracts as needed)

---

### 1.3 Design rationale

Explain key architectural decisions:

**Why did you choose this architecture?**

[Your answer - minimum 150 words]

---

**What alternatives did you consider and why did you reject them?**

[Your answer]

---

**How does your design promote modularity, reusability, or upgradability?**

[Your answer]

---

## 2. Contract Interfaces (30%)

### 2.1 State variables

For each contract, list all state variables:

**Contract 1: _________________________**

```solidity
// State Variables

// Example:
// mapping(address => uint256) public balances;
// address public owner;
// uint256 public totalSupply;

[Insert your state variables here]
```

**Data structure justifications**:

| Variable | Type | Why this type? |
|----------|------|----------------|
| Example: balances | mapping(address => uint256) | Efficient O(1) lookup for user balances |
| | | |
| | | |

---

**Contract 2: _________________________**

```solidity
// State Variables

[Insert your state variables here]
```

(Repeat for each contract)

---

### 2.2 Function signatures

For each contract, list all functions with complete signatures:

**Contract 1: _________________________**

```solidity
// Constructor
constructor(parameters) { }

// External/Public Functions

// Example:
// function transfer(address to, uint256 amount) external returns (bool);
// function approve(address spender, uint256 amount) external returns (bool);

[Insert your function signatures here]

// Internal Functions

[Insert internal helper functions here]

// View/Pure Functions

[Insert view/pure functions here]
```

---

**Function documentation**:

For each major function, provide:

| Function | Purpose | Parameters | Returns | Access Control |
|----------|---------|------------|---------|----------------|
| Example: mint() | Creates new tokens | address to, uint256 amount | bool success | onlyOwner |
| | | | | |
| | | | | |

---

### 2.3 Events

List all events your contracts will emit:

**Contract 1: _________________________**

```solidity
// Events

// Example:
// event Transfer(address indexed from, address indexed to, uint256 amount);
// event Approval(address indexed owner, address indexed spender, uint256 amount);

[Insert your events here]
```

**Event justifications**:

| Event | When emitted | Why needed |
|-------|-------------|------------|
| Example: Transfer | When tokens change ownership | Track token movements for frontend, compliance |
| | | |
| | | |

---

### 2.4 Custom errors (Solidity 0.8+)

Define custom errors for gas-efficient error handling:

```solidity
// Custom Errors

// Example:
// error InsufficientBalance(uint256 available, uint256 required);
// error Unauthorized(address caller);

[Insert your custom errors here]
```

---

## 3. Data Structures & Storage (15%)

### 3.1 On-chain data

What data will you store on-chain? Why?

| Data | Storage Location | Justification |
|------|-----------------|---------------|
| Example: Token balances | Mapping in smart contract | Core protocol state, must be on-chain |
| | | |
| | | |

---

### 3.2 Off-chain data

What data will you store off-chain? Where and why?

| Data | Storage Solution | Justification |
|------|-----------------|---------------|
| Example: NFT images | IPFS | Too large/expensive for on-chain, IPFS provides decentralization |
| | | |
| | | |

---

### 3.3 Data flow diagram

Show how data moves through your system:
- User input -> Smart contract -> Storage
- Smart contract -> Events -> Frontend
- Off-chain data retrieval flows

[Insert data flow diagram here]

---

## 4. Security Considerations (25%)

### 4.1 Identified risks

List potential security vulnerabilities and how you'll address them:

**Risk 1: Reentrancy**
- Vulnerable functions: ___________________________
- Mitigation strategy: ___________________________ (e.g., ReentrancyGuard, Checks-Effects-Interactions)

**Risk 2: Integer Overflow/Underflow**
- Vulnerable operations: ___________________________
- Mitigation strategy: ___________________________ (e.g., Solidity 0.8+, SafeMath)

**Risk 3: Access Control**
- Sensitive functions: ___________________________
- Mitigation strategy: ___________________________ (e.g., Ownable, AccessControl, custom modifiers)

**Risk 4: Front-running/MEV**
- Vulnerable transactions: ___________________________
- Mitigation strategy: ___________________________

**Risk 5: Oracle Manipulation** (if using oracles)
- Oracle dependencies: ___________________________
- Mitigation strategy: ___________________________ (e.g., Chainlink, multiple sources)

(Add more risks as relevant to your project)

---

### 4.2 Access control design

Who can call which functions?

| Function | Allowed Callers | Modifier/Check |
|----------|----------------|----------------|
| Example: mint() | Contract owner only | onlyOwner modifier |
| Example: transfer() | Any token holder | require(balance >= amount) |
| | | |
| | | |

---

### 4.3 Input validation

How will you validate inputs to prevent invalid states?

**Function: _________________________**
- Validation 1: ___________________________
- Validation 2: ___________________________

(Repeat for critical functions)

---

### 4.4 Emergency procedures

**Pause mechanism**:
- Do you need a pause function? [ ] Yes [ ] No
- If yes, who can pause? ___________________________
- Which functions are paused? ___________________________

**Upgrade strategy**:
- Are contracts upgradeable? [ ] Yes [ ] No
- If yes, what pattern? ___________________________ (e.g., Proxy pattern, Diamond pattern)
- If no, how will you handle bugs? ___________________________

---

## 5. Gas Optimization Strategy (10%)

### 5.1 Expensive operations

Identify gas-intensive operations in your contracts:

1. Operation: ___________________________
   - Estimated cost: ___________________________ gas
   - Optimization approach: ___________________________

2. Operation: ___________________________
   - Estimated cost: ___________________________ gas
   - Optimization approach: ___________________________

---

### 5.2 Storage optimization

How are you minimizing storage costs?

- Technique 1: ___________________________ (e.g., packing variables, using uint256 vs uint8)
- Technique 2: ___________________________
- Technique 3: ___________________________

---

### 5.3 Trade-offs

What trade-offs are you making between gas costs and other factors (readability, security, functionality)?

[Your answer here]

---

## 6. Testing Strategy (10%)

### 6.1 Unit tests

What will you test at the unit level?

**Contract 1: _________________________**

Test cases:
1. Test: ___________________________ (e.g., "should mint tokens correctly")
   - Setup: ___________________________
   - Expected result: ___________________________

2. Test: ___________________________
   - Setup: ___________________________
   - Expected result: ___________________________

(List 3-5 key tests per contract)

---

### 6.2 Integration tests

How will you test contract interactions?

Scenario 1: ___________________________
- Contracts involved: ___________________________
- Test flow: ___________________________
- Expected outcome: ___________________________

(List 2-3 integration test scenarios)

---

### 6.3 Edge cases

What edge cases will you test?

1. Edge case: ___________________________ (e.g., "transfer with zero amount")
   - Expected behavior: ___________________________

2. Edge case: ___________________________
   - Expected behavior: ___________________________

3. Edge case: ___________________________ (e.g., "overflow/underflow scenarios")
   - Expected behavior: ___________________________

---

## 7. Standards Compliance (10%)

### 7.1 Implementing standards

Which ERC standards are you implementing?

- [ ] ERC-20 (Fungible Tokens)
- [ ] ERC-721 (Non-Fungible Tokens)
- [ ] ERC-1155 (Multi-Token Standard)
- [ ] ERC-2981 (NFT Royalty Standard)
- [ ] Other: ___________________________

---

### 7.2 Standard compliance verification

How will you ensure compliance?

Standard: ERC-___
- Required functions: ___________________________ (list all)
- Required events: ___________________________ (list all)
- Optional extensions: ___________________________ (which are you implementing?)

---

### 7.3 Custom extensions

Are you adding any custom functionality beyond the standard?

Extension 1: ___________________________
- Purpose: ___________________________
- Does it maintain standard compliance? [ ] Yes [ ] No

---

## 8. Dependencies & Libraries (5%)

### 8.1 External libraries

What libraries will you use?

1. Library: ___________________________ (e.g., OpenZeppelin Contracts)
   - Version: ___________________________
   - Used for: ___________________________
   - Specific imports: ___________________________

2. Library: ___________________________
   - Version: ___________________________
   - Used for: ___________________________

---

### 8.2 Audited vs. custom code

| Component | Audited Library | Custom Implementation |
|-----------|-----------------|----------------------|
| Example: Access control | OpenZeppelin Ownable | |
| Example: Token standard | OpenZeppelin ERC20 | |
| Example: Business logic | | Custom implementation |
| | | |

**Justification for custom implementations**:

[Explain why you're writing custom code instead of using libraries]

---

## 9. Deployment Plan (5%)

### 9.1 Deployment order

In what order will you deploy contracts? Why?

1. Contract: ___________________________
   - Reason for order: ___________________________

2. Contract: ___________________________
   - Reason for order: ___________________________

---

### 9.2 Initialization

What initialization is needed post-deployment?

Contract: ___________________________
- Initialization function: ___________________________
- Parameters: ___________________________
- Who can call: ___________________________

---

### 9.3 Network selection

**Primary testnet**: ___________________________ (e.g., Sepolia)
- Justification: ___________________________

**Alternative networks** (if any): ___________________________

---

## 10. Open Questions & Risks (5%)

### 10.1 Unresolved design decisions

What design questions remain open?

1. Question: ___________________________
   - Options being considered: ___________________________
   - Target resolution date: ___________________________

2. Question: ___________________________
   - Options being considered: ___________________________

---

### 10.2 Technical risks

What could go wrong with this design?

Risk 1: ___________________________
- Impact: ___________________________
- Mitigation: ___________________________

Risk 2: ___________________________
- Impact: ___________________________
- Mitigation: ___________________________

---

## Appendix: Code Snippets (Optional)

If helpful, include draft interface code:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IYourContract {
    // Function signatures
}
```

---

## Grading Rubric (for reference)

| Criterion | Points | Your Score |
|-----------|--------|------------|
| Architectural soundness | 35% | |
| Completeness of design | 25% | |
| Security awareness | 25% | |
| Documentation quality | 15% | |
| **Total** | **100%** | |

---

## Submission Instructions

1. Save this document as: `M2_Design_TeamName.pdf`
2. Create GitHub repository with:
   - `/contracts` folder with interface files (`.sol`)
   - `/docs` folder with this design document
   - `README.md` with project overview
3. Submit PDF via Moodle AND GitHub repo link by Week 6 deadline
4. Late submissions: 10% penalty per day (max 3 days)

---

## Instructor Feedback Section

**Strengths**:

---

**Areas for Improvement**:

---

**Security Concerns**:

---

**Recommendations**:

---

**Grade**: _______ / 100

**Instructor Signature**: ___________________ **Date**: _______________
