# Quiz 3: Tokens & NFTs
## BSc Blockchain, Crypto Economy & NFTs

**Lectures Covered**: L17-L24 (Token Standards through NFT Technical Deep Dive)
**Duration**: 30 minutes
**Total Points**: 100 points
**Question Types**: 6 multiple choice (8 pts each), 4 short answer (13 pts each)

---

## Multiple Choice Questions (48 points total)

### Question 1 (8 points)
**Topic**: ERC-20 Standard

Which of the following is NOT a required function in the ERC-20 token standard?

A) transfer()
B) approve()
C) mint()
D) balanceOf()

**Correct Answer**: C

**Explanation**: The ERC-20 standard requires: totalSupply(), balanceOf(), transfer(), transferFrom(), approve(), and allowance(). The mint() function is NOT part of the standard, though many implementations include it for token creation. The standard only defines how tokens behave once they exist, not how they are created.

---

### Question 2 (8 points)
**Topic**: NFT Standards

What is the key technical difference between ERC-721 and ERC-1155 token standards?

A) ERC-721 tokens are fungible, ERC-1155 tokens are not
B) ERC-721 represents individual unique tokens, while ERC-1155 can manage multiple token types (both fungible and non-fungible) in a single contract
C) ERC-1155 uses less gas than ERC-721 for single transfers
D) ERC-721 was created after ERC-1155

**Correct Answer**: B

**Explanation**: ERC-721 represents individual, unique NFTs (one contract per collection). ERC-1155 is a multi-token standard that can manage multiple token types (both fungible and non-fungible) in a single contract, enabling batch transfers and more efficient gas usage for multi-token operations.

---

### Question 3 (8 points)
**Topic**: Token Metadata

Where is NFT metadata typically stored for maximum decentralization?

A) Directly in the smart contract storage
B) On centralized servers like AWS
C) On IPFS (InterPlanetary File System) or Arweave
D) In the Ethereum transaction data

**Correct Answer**: C

**Explanation**: While contract storage is fully decentralized, it's extremely expensive for large metadata (images, attributes). IPFS and Arweave provide decentralized, permanent storage solutions. Centralized servers risk data loss or censorship. The smart contract typically stores only a reference (URI or IPFS hash) to the metadata.

---

### Question 4 (8 points)
**Topic**: Token Allowances

In the ERC-20 standard, what does the approve() function enable?

A) It allows the contract owner to freeze tokens
B) It permits another address to spend tokens on behalf of the token holder up to a specified amount
C) It validates that a transaction is legitimate
D) It converts tokens to ETH

**Correct Answer**: B

**Explanation**: The approve() function allows a token holder to authorize another address (spender) to transfer up to a specified amount of tokens on their behalf. This is commonly used for DEX interactions, where users approve a DEX contract to spend their tokens for swaps.

---

### Question 5 (8 points)
**Topic**: NFT Standards

What does EIP-2981 standardize for NFTs?

A) Metadata format
B) Royalty payments
C) Minting mechanisms
D) Transfer restrictions

**Correct Answer**: B

**Explanation**: EIP-2981 is the NFT Royalty Standard. It provides a standardized way to retrieve royalty payment information, allowing marketplaces to automatically pay creators a percentage of secondary sales. It defines a royaltyInfo() function that returns the recipient address and amount.

---

### Question 6 (8 points)
**Topic**: Token Fungibility

Which statement best describes "fungibility" in the context of tokens?

A) Tokens that can be exchanged on any blockchain
B) Tokens that are interchangeable and of equal value (like currency units)
C) Tokens that cannot be transferred
D) Tokens that increase in value over time

**Correct Answer**: B

**Explanation**: Fungible tokens are interchangeable and mutually substitutable - each unit is identical and has the same value (like dollar bills or ERC-20 tokens). Non-fungible tokens (NFTs) are unique and not interchangeable (each has distinct properties and value).

---

## Short Answer Questions (52 points total)

### Question 7 (13 points)
**Topic**: ERC-20 Implementation

Explain the relationship between approve(), allowance(), and transferFrom() in the ERC-20 standard. Why is this three-function pattern necessary?

**Model Answer** (for grading reference):

The three-function pattern enables third-party transfers:

**approve(spender, amount)**:
- Token holder calls this to authorize a spender address to transfer up to 'amount' tokens on their behalf
- Records the allowance in a mapping: owner -> spender -> amount
- Emits Approval event

**allowance(owner, spender)**:
- View function that returns how much a spender is still allowed to transfer from owner's balance
- Anyone can query this

**transferFrom(from, to, amount)**:
- Spender calls this to transfer tokens from the authorizing owner to a recipient
- Requires that allowance[from][msg.sender] >= amount
- Decreases the allowance by the transferred amount
- Transfers tokens from 'from' to 'to'

**Why necessary**:
This pattern enables complex DeFi interactions without tokens leaving user custody until needed. For example:
- User approves Uniswap to spend 100 USDC
- User initiates swap on Uniswap
- Uniswap contract uses transferFrom() to pull the exact needed USDC amount
- User maintains control until the swap actually executes

Without this pattern, users would need to first transfer tokens to contracts (risky) or contracts couldn't interact with user tokens.

**Grading Criteria**:
- 13 points: Explains all three functions, their interaction, and why pattern is needed
- 9-12 points: Good explanation but missing some details or use case
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

### Question 8 (13 points)
**Topic**: NFT Metadata Standards

Describe the standard metadata format for ERC-721 NFTs. What fields are typically included, and why is standardization important for NFT marketplaces?

**Model Answer** (for grading reference):

**Standard Metadata Format** (based on OpenSea/community standards):

The tokenURI() function returns a URI pointing to a JSON file with this structure:

```json
{
  "name": "Token Name",
  "description": "Description of the NFT",
  "image": "ipfs://...",
  "attributes": [
    {
      "trait_type": "Category",
      "value": "Example"
    }
  ],
  "external_url": "https://...",
  "background_color": "FFFFFF"
}
```

**Standard Fields**:
- **name**: NFT title
- **description**: Text description
- **image**: URI to the visual asset (IPFS, Arweave, or HTTP)
- **attributes**: Array of traits/properties for rarity and filtering
- **external_url**: Link to more information
- **animation_url** (optional): For video/audio/interactive NFTs
- **background_color** (optional): Display preference

**Why Standardization Matters**:
1. **Interoperability**: Marketplaces (OpenSea, Blur, LooksRare) can display any NFT without custom integration
2. **Discovery**: Standardized attributes enable filtering and search
3. **User Experience**: Consistent presentation across platforms
4. **Developer Experience**: Easy integration for wallets and dApps
5. **Composability**: Other contracts/apps can parse metadata predictably

Without standards, each project would need custom parsers, fragmenting the ecosystem.

**Grading Criteria**:
- 13 points: Describes metadata structure + explains importance with specific reasons
- 9-12 points: Good description but less comprehensive on importance
- 6-8 points: Basic understanding but missing details
- 3-5 points: Vague or incomplete
- 0-2 points: Incorrect or no meaningful answer

---

### Question 9 (13 points)
**Topic**: ERC-1155 Multi-Token Standard

Explain the advantages of ERC-1155 over ERC-721. Provide at least two specific use cases where ERC-1155 would be preferable.

**Model Answer** (for grading reference):

**ERC-1155 Advantages**:

1. **Multi-Token Management**:
   - Single contract can manage unlimited token types (both fungible and non-fungible)
   - ERC-721 requires one contract per collection

2. **Batch Operations**:
   - safeBatchTransferFrom() allows transferring multiple token types in one transaction
   - Significantly reduces gas costs for multi-item transfers
   - ERC-721 requires separate transactions for each NFT

3. **Gas Efficiency**:
   - Less redundant bytecode deployment
   - Batch operations save gas on multiple transfers
   - More efficient storage patterns

4. **Flexibility**:
   - Can represent both fungible (e.g., 1000 identical gold coins) and non-fungible items (unique weapons)
   - Each token ID can have its own supply (1 for unique, 1000+ for fungible)

5. **Built-in Safety**:
   - safeTransferFrom() ensures recipient can handle tokens
   - Prevents accidental burns to non-compatible contracts

**Use Cases Where ERC-1155 is Preferable**:

**Use Case 1: Gaming**
- Game items include both unique assets (legendary sword - supply of 1) and consumables (health potions - supply of 10,000)
- Players transfer multiple items together (sword + potions + armor) in one transaction
- Single contract manages entire game economy
- Example: Enjin ecosystem, Axie Infinity items

**Use Case 2: Event Ticketing**
- General admission tickets are fungible (1000 identical tickets)
- VIP tickets are semi-fungible (100 identical VIP passes)
- Backstage passes are unique NFTs (supply of 1 each with holder name)
- Batch transfer enables reselling multiple ticket types together
- Single contract for entire event

**Use Case 3: Digital Art Collections with Editions**
- Artist creates 1 unique original (token ID 1, supply 1)
- Artist creates 100 limited edition prints (token ID 2, supply 100)
- All managed in single contract with efficient storage

**Grading Criteria**:
- 13 points: Explains advantages clearly + provides 2+ detailed, appropriate use cases
- 9-12 points: Good explanation but use cases less detailed
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or weak use cases
- 0-2 points: Incorrect or no meaningful answer

---

### Question 10 (13 points)
**Topic**: Token Security

What is the "approve race condition" vulnerability in ERC-20 tokens, and how can it be mitigated? Provide a specific example of how the attack works.

**Model Answer** (for grading reference):

**Approve Race Condition** (also called "approve/transferFrom attack"):

**The Vulnerability**:
When a token holder wants to change an existing allowance from one amount to another, a malicious spender can exploit transaction ordering to spend both the old and new allowance amounts.

**Attack Example**:

1. Alice approves Bob to spend 100 tokens: approve(Bob, 100)
2. Later, Alice wants to change this to 50 tokens: approve(Bob, 50)
3. Bob monitors the mempool and sees Alice's new approval transaction
4. Bob front-runs Alice's transaction by calling transferFrom() to spend the original 100 tokens
5. Alice's transaction executes, setting allowance to 50
6. Bob now calls transferFrom() again to spend the new 50 tokens
7. Bob has spent 150 tokens total, though Alice only intended to allow 50

**Why it happens**:
- Blockchain transaction ordering is uncertain
- approve() overwrites the previous value rather than adjusting it
- No built-in protection against this race condition

**Mitigation Strategies**:

1. **Set to Zero First** (Recommended by ERC-20):
   ```solidity
   approve(spender, 0);  // First transaction
   approve(spender, newAmount);  // Second transaction
   ```
   This prevents exploitation but requires two transactions.

2. **Use increaseAllowance() and decreaseAllowance()**:
   ```solidity
   increaseAllowance(spender, additionalAmount);
   decreaseAllowance(spender, subtractedAmount);
   ```
   OpenZeppelin's ERC-20 implementation includes these functions that adjust allowances rather than overwriting, preventing the race condition.

3. **Check Current Allowance**:
   Some implementations allow specifying the expected current allowance:
   ```solidity
   approveAndCall(spender, currentAllowance, newAllowance);
   ```
   Transaction reverts if currentAllowance doesn't match.

**Best Practice**:
Use OpenZeppelin's ERC-20 implementation with increaseAllowance/decreaseAllowance instead of directly using approve() for allowance changes.

**Grading Criteria**:
- 13 points: Clear explanation of vulnerability + specific example + mitigation methods
- 9-12 points: Good explanation but missing some details
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

## Answer Key Summary

| Question | Type | Answer | Points |
|----------|------|--------|--------|
| Q1 | MC | C | 8 |
| Q2 | MC | B | 8 |
| Q3 | MC | C | 8 |
| Q4 | MC | B | 8 |
| Q5 | MC | B | 8 |
| Q6 | MC | B | 8 |
| Q7 | SA | See model answer | 13 |
| Q8 | SA | See model answer | 13 |
| Q9 | SA | See model answer | 13 |
| Q10 | SA | See model answer | 13 |
| **Total** | | | **100** |

---

## Topics Covered

**Lectures L17-L24**:
- Token fundamentals and fungibility
- ERC-20 standard (interface, functions, events)
- ERC-20 implementation and security
- NFT introduction and use cases
- ERC-721 standard (interface, ownership)
- ERC-1155 multi-token standard
- NFT metadata standards and storage (IPFS, Arweave)
- Token URI and metadata JSON format
- EIP-2981 royalty standard
- Approve/allowance mechanism
- Token security (approve race condition, reentrancy)
- Batch operations and gas optimization

---

## Study Recommendations

- Review lecture slides L17-L24
- Understand ERC-20 interface completely (all 6 functions)
- Know the differences between ERC-721 and ERC-1155
- Study NFT metadata format and storage solutions
- Practice implementing basic ERC-20 and ERC-721 contracts
- Understand approve/transferFrom pattern and its vulnerabilities
- Review OpenZeppelin implementations as reference
- Explore NFT marketplaces to see standards in action
