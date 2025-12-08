# Quiz 5: DeFi (Decentralized Finance)
## BSc Blockchain, Crypto Economy & NFTs

**Lectures Covered**: L33-L40 (DeFi Introduction through Advanced DeFi Concepts)
**Duration**: 30 minutes
**Total Points**: 100 points
**Question Types**: 6 multiple choice (8 pts each), 4 short answer (13 pts each)

---

## Multiple Choice Questions (48 points total)

### Question 1 (8 points)
**Topic**: DeFi Fundamentals

What is the primary advantage of DeFi (Decentralized Finance) over traditional finance?

A) Guaranteed higher returns on investments
B) Permissionless access, transparency, and composability without intermediaries
C) Complete anonymity for all transactions
D) Government insurance on deposits

**Correct Answer**: B

**Explanation**: DeFi's core advantages are: permissionless access (anyone with internet can participate), transparency (all transactions visible on-chain), composability (protocols interoperate), and disintermediation (no banks/brokers needed). DeFi does NOT guarantee higher returns, complete anonymity, or FDIC-like insurance.

---

### Question 2 (8 points)
**Topic**: Automated Market Makers (AMMs)

In a constant product AMM like Uniswap (x * y = k), what happens to the price when someone buys token X from the pool?

A) The price of token X decreases
B) The price of token X stays the same
C) The price of token X increases
D) The pool needs to be rebalanced by an administrator

**Correct Answer**: C

**Explanation**: When someone buys token X, they add token Y to the pool and remove token X. This decreases x and increases y. To maintain the constant k, the ratio y/x increases, which means the price of X (in terms of Y) increases. This is how AMMs automatically adjust prices based on supply and demand without order books or administrators.

---

### Question 3 (8 points)
**Topic**: Liquidity Pools

What is "impermanent loss" for liquidity providers in AMMs?

A) The loss of tokens due to a smart contract hack
B) The opportunity cost of providing liquidity versus simply holding tokens, which becomes permanent when you withdraw
C) The transaction fees charged by the AMM
D) The slippage experienced during large trades

**Correct Answer**: B

**Explanation**: Impermanent loss occurs when the price ratio of pooled tokens changes compared to when you deposited them. You would have more value if you had simply held the tokens instead of providing liquidity. It's "impermanent" while you remain in the pool (can reverse if prices revert), but becomes permanent when you withdraw. It's a key risk for liquidity providers.

---

### Question 4 (8 points)
**Topic**: Lending Protocols

In DeFi lending protocols like Aave or Compound, what determines the interest rate for borrowing?

A) A central administrator sets fixed rates
B) Supply and demand dynamics - utilization rate of the pool
C) The credit score of the borrower
D) Government bond yields

**Correct Answer**: B

**Explanation**: DeFi lending uses algorithmic interest rates based on utilization (borrowed / supplied). High utilization means high demand for borrowing, which increases rates to incentivize more supply. Low utilization means low rates to encourage borrowing. No credit checks, KYC, or centralized rate-setting - purely algorithmic based on supply/demand.

---

### Question 5 (8 points)
**Topic**: Collateralization

Why do most DeFi lending protocols require over-collateralization (borrowing less than your collateral value)?

A) To comply with banking regulations
B) To protect against price volatility and ensure loans remain sufficiently collateralized despite market fluctuations
C) To make more profit for the protocol
D) To prevent anyone from borrowing

**Correct Answer**: B

**Explanation**: Over-collateralization (e.g., deposit 150 worth of ETH to borrow 100 worth of DAI) creates a safety buffer against price volatility. If ETH price drops, the loan remains collateralized. This protects lenders from defaults. Under-collateralized loans would require trust/credit checks, contradicting DeFi's permissionless ethos.

---

### Question 6 (8 points)
**Topic**: Flash Loans

What makes flash loans unique in DeFi?

A) They have extremely low interest rates
B) They must be borrowed and repaid within a single transaction, with no collateral required
C) They can only be used by verified institutions
D) They take a very long time to process

**Correct Answer**: B

**Explanation**: Flash loans are uncollateralized loans that must be borrowed and fully repaid within one atomic transaction. If repayment fails, the entire transaction reverts as if the loan never happened. This eliminates default risk while enabling arbitrage, liquidations, and collateral swaps without upfront capital.

---

## Short Answer Questions (52 points total)

### Question 7 (13 points)
**Topic**: Automated Market Makers

Explain how a constant product AMM (x * y = k) works. Using a simple example, show how the price changes when someone makes a trade.

**Model Answer** (for grading reference):

**Constant Product AMM (x * y = k)**:

A constant product AMM maintains a liquidity pool with two tokens where the product of their quantities remains constant.

**Formula**: x * y = k

Where:
- x = quantity of token A in pool
- y = quantity of token B in pool
- k = constant product

**Price Determination**:
The price of token A in terms of token B is: Price_A = y / x
The price of token B in terms of token A is: Price_B = x / y

**Example**:

**Initial State**:
- Pool contains: 100 ETH (x) and 200,000 USDC (y)
- Constant k = 100 * 200,000 = 20,000,000
- Current price: 1 ETH = 200,000/100 = 2,000 USDC

**Trade**: Alice wants to buy 10 ETH

**Step 1**: Calculate new pool state after removing 10 ETH:
- New x = 100 - 10 = 90 ETH
- k must stay constant: 90 * y_new = 20,000,000
- y_new = 20,000,000 / 90 = 222,222.22 USDC

**Step 2**: Alice must add USDC to maintain k:
- USDC to add = 222,222.22 - 200,000 = 22,222.22 USDC
- Alice pays 22,222.22 USDC for 10 ETH
- Average price: 2,222.22 USDC per ETH (higher than initial 2,000)

**Step 3**: New pool state:
- 90 ETH and 222,222.22 USDC
- New price: 1 ETH = 222,222.22/90 = 2,469 USDC
- Price increased due to reduced ETH supply

**Key Properties**:
- Price automatically adjusts based on trades
- Larger trades cause more price impact (slippage)
- No order book needed
- Always liquidity (though at varying prices)
- Arbitrageurs keep pool prices aligned with external markets

**Grading Criteria**:
- 13 points: Clear explanation of formula + worked example showing price change
- 9-12 points: Good explanation but example less detailed or minor errors
- 6-8 points: Basic understanding but incomplete example
- 3-5 points: Vague or significant errors
- 0-2 points: Incorrect or no meaningful answer

---

### Question 8 (13 points)
**Topic**: DeFi Composability

What is "composability" in DeFi, and why is it considered a superpower? Provide a specific example of how multiple DeFi protocols can be combined.

**Model Answer** (for grading reference):

**Composability** ("Money Legos"):

Composability is the ability of DeFi protocols to seamlessly interact and build on top of each other like LEGO blocks. Smart contracts are permissionless and open, allowing anyone to integrate them without asking permission.

**Why It's a Superpower**:

1. **Rapid Innovation**: New protocols leverage existing infrastructure instead of rebuilding
2. **Network Effects**: Each new protocol adds value to existing ones
3. **User Benefits**: Complex financial strategies become accessible to anyone
4. **Capital Efficiency**: Same capital can be used across multiple protocols simultaneously
5. **Permissionless**: No business development deals or partnerships needed
6. **Transparency**: All integrations visible on-chain

**Example: Multi-Protocol Strategy**

**Scenario**: Alice wants to maximize yield on her ETH

**Step 1 - Deposit ETH in Lido**:
- Alice deposits 10 ETH in Lido (liquid staking protocol)
- Receives 10 stETH (staked ETH earning ~4% APR)
- stETH is a token representing her staked ETH

**Step 2 - Use stETH as Collateral in Aave**:
- Alice deposits stETH into Aave (lending protocol)
- Borrows DAI (stablecoin) against her stETH collateral
- Borrows 50% LTV = 10,000 DAI (assuming stETH = 2,000)
- Pays ~3% APR interest on borrowed DAI

**Step 3 - Provide Liquidity on Curve**:
- Alice adds borrowed DAI to Curve DAI/USDC pool (stablecoin AMM)
- Receives LP tokens representing her liquidity position
- Earns trading fees + CRV token rewards (~5% APR)

**Step 4 - Stake LP Tokens in Convex**:
- Alice stakes Curve LP tokens in Convex (yield optimizer)
- Earns additional CVX tokens on top of CRV rewards
- Total additional yield: ~8% APR

**Net Result**:
- Original ETH still earning staking rewards in Lido: ~4%
- DAI liquidity provision earning: ~8%
- Borrowing cost: -3%
- Net additional yield: ~5% on top of ETH staking
- Capital efficiency: Same 10 ETH used across 4 protocols

**Risks**:
- Smart contract risk in each protocol (4 contracts = 4 attack surfaces)
- Liquidation risk if stETH price drops
- Impermanent loss in Curve pool (minimal for stablecoins)
- Cascading failures if one protocol is exploited

**This demonstrates composability**: Alice combined Lido + Aave + Curve + Convex without needing permission, creating a sophisticated strategy that would be impossible in traditional finance.

**Other Examples**:
- Flash loan from Aave -> arbitrage on Uniswap -> repay in same transaction
- Borrow on Compound -> farm on Yearn -> auto-compound rewards
- Mint DAI on Maker -> stake on Curve -> use receipt token in Convex

**Grading Criteria**:
- 13 points: Clear definition + detailed multi-protocol example with explanation
- 9-12 points: Good definition and example but less comprehensive
- 6-8 points: Basic understanding but weak example
- 3-5 points: Vague or superficial
- 0-2 points: Incorrect or no meaningful answer

---

### Question 9 (13 points)
**Topic**: Liquidations

Explain how liquidation works in DeFi lending protocols. Why is it necessary, and what role do liquidators play?

**Model Answer** (for grading reference):

**Liquidation in DeFi Lending**:

Liquidation is the process of forcibly selling a borrower's collateral when its value falls below a required threshold, protecting lenders from losses.

**How It Works**:

**Setup**:
- Alice deposits 1 ETH (2,000) as collateral in Aave
- Borrows 1,000 DAI at 150% collateralization ratio
- Health Factor = (Collateral Value * Liquidation Threshold) / Borrowed Value
- Initial Health Factor = (2,000 * 0.80) / 1,000 = 1.6 (healthy)

**Price Drop Scenario**:
- ETH price drops from 2,000 to 1,300
- New collateral value = 1,300
- Health Factor = (1,300 * 0.80) / 1,000 = 1.04 (approaching danger)
- If ETH drops to 1,250: Health Factor = 1.0 (liquidation threshold)

**Liquidation Process**:

1. **Trigger**: When Health Factor < 1.0, position becomes eligible for liquidation

2. **Liquidator Action**:
   - Anyone (liquidator bot) can repay part of Alice's debt
   - In exchange, liquidator receives Alice's collateral at a discount (e.g., 5-10%)
   - Example: Liquidator repays 500 DAI, receives 550 worth of ETH

3. **Result**:
   - Alice's debt reduced by 500 DAI (now owes 500 DAI)
   - Alice's collateral reduced (some ETH sold)
   - Liquidation penalty paid by Alice (typically 5-10%)
   - Alice's position is healthier (higher health factor)

4. **Full vs Partial**:
   - Protocols usually allow partial liquidation (e.g., 50% of debt)
   - Prevents over-liquidation and gives borrowers chance to recover

**Why Liquidation is Necessary**:

1. **Protect Lenders**: Ensures borrowed funds remain fully backed by collateral
2. **System Solvency**: Prevents protocol insolvency if collateral values drop
3. **Risk Management**: Maintains over-collateralization of all loans
4. **Market Confidence**: Lenders trust they can withdraw funds because loans are secure

**Without liquidations**:
- Collateral could become worth less than debt
- Borrowers could walk away (default)
- Lenders would lose funds
- Protocol would become insolvent

**Role of Liquidators**:

**Who They Are**:
- Usually automated bots run by sophisticated operators
- Compete to liquidate positions first (profit opportunity)
- Provide essential service to protocol health

**What They Do**:
1. **Monitor Positions**: Constantly check health factors of all loans
2. **Execute Liquidations**: Trigger liquidation when threshold breached
3. **Flash Loan Integration**: Often use flash loans to liquidate without upfront capital:
   - Borrow DAI via flash loan
   - Repay borrower's debt
   - Receive collateral at discount
   - Swap collateral for DAI
   - Repay flash loan + profit
   - All in one transaction

**Incentives**:
- Earn liquidation bonus (5-10% discount on collateral)
- Example: Pay 1,000 DAI to receive 1,100 worth of ETH = 100 profit
- Competitive market: fastest bots win

**Example Transaction Flow**:

```
1. Flash loan 10,000 DAI from Aave
2. Liquidate underwater position (repay 10,000 DAI debt)
3. Receive 11,000 worth of ETH collateral (10% bonus)
4. Swap ETH for DAI on Uniswap, receive 10,900 DAI
5. Repay flash loan 10,000 DAI
6. Profit: 900 DAI (minus gas fees)
```

**Edge Cases**:

- **Cascading Liquidations**: Large price drops trigger mass liquidations, causing more sell pressure
- **Network Congestion**: High gas fees during volatility can make small liquidations unprofitable
- **Bad Debt**: If liquidations are too slow, collateral may drop below debt value (protocol loss)

**Grading Criteria**:
- 13 points: Comprehensive explanation of mechanism, necessity, and liquidator role with example
- 9-12 points: Good explanation but missing some details
- 6-8 points: Basic understanding but incomplete
- 3-5 points: Vague or superficial
- 0-2 points: Incorrect or no meaningful answer

---

### Question 10 (13 points)
**Topic**: Stablecoins

Compare algorithmic stablecoins with collateral-backed stablecoins. What are the key mechanisms, benefits, and risks of each approach?

**Model Answer** (for grading reference):

**Stablecoin Comparison**:

Stablecoins aim to maintain a stable value (usually pegged to 1 USD). Different mechanisms achieve this goal with varying trade-offs.

---

**1. COLLATERAL-BACKED STABLECOINS**

**Types**:

**A) Fiat-Collateralized** (USDC, USDT):
- Backed 1:1 by USD in bank accounts
- Centralized issuer holds reserves
- Redeemable for fiat

**B) Crypto-Collateralized** (DAI):
- Backed by cryptocurrency (ETH, WBTC, etc.)
- Over-collateralized (e.g., 150% ratio)
- Decentralized, permissionless

**Mechanism (Using DAI as Example)**:

1. **Minting**: User deposits 3,000 worth of ETH, borrows 2,000 DAI (150% collateral ratio)
2. **Stability**: Value maintained through arbitrage and liquidations
3. **Redemption**: User repays 2,000 DAI + interest, retrieves ETH collateral
4. **Price Stability**:
   - If DAI > 1: Incentive to mint more DAI (sell at premium), increases supply, price drops
   - If DAI < 1: Incentive to buy DAI to repay debt (cheaper), decreases supply, price rises

**Benefits**:
- Proven stability mechanism
- Transparent reserves (on-chain for crypto-backed)
- Battle-tested (DAI, USDC have multi-year track records)
- Capital efficiency for users (leverage on collateral)

**Risks**:
- **Fiat-backed**: Centralization, regulatory risk, bank risk, requires trust in issuer
- **Crypto-backed**: Collateral volatility, liquidation cascades, capital inefficiency (need 150+ for 100 stablecoin)
- Smart contract risk
- Scalability limited by available collateral

---

**2. ALGORITHMIC STABLECOINS**

**Mechanism**: Use algorithms and incentive mechanisms to maintain peg without (or with minimal) collateral.

**Type A: Rebase Mechanism** (e.g., Ampleforth):
- Supply expands/contracts based on price
- If price > 1: increase supply (dilute holders)
- If price < 1: decrease supply (concentrate holders)

**Type B: Seigniorage/Multi-Token** (e.g., Terra/Luna - FAILED):
- Two tokens: stablecoin (UST) and volatile token (LUNA)
- Arbitrage mechanism maintains peg:
  - UST > 1: Burn 1 of LUNA to mint 1 UST, sell for profit
  - UST < 1: Burn 1 UST to mint 1 of LUNA, buy UST for profit
- Relies on confidence and demand for volatile token

**Type C: Collateralized Debt Position with Fractional Reserve** (e.g., Frax):
- Partially collateralized (e.g., 85% USDC + 15% FXS tokens)
- Algorithm adjusts collateral ratio based on market conditions

**Benefits**:
- Capital efficiency (no over-collateralization)
- Scalability (not limited by collateral supply)
- Decentralized (no fiat backing)
- Potential for innovative mechanisms

**Risks**:
- **Death Spiral**: Loss of confidence can trigger collapse
  - Example: Terra/Luna (May 2022) - UST lost peg, redemptions for LUNA crashed LUNA price, further reducing UST backing
- Untested at scale
- Complex game theory
- Vulnerable to bank runs
- Lack of proven stability during extreme volatility

---

**Comparison Table**:

| Aspect | Collateral-Backed | Algorithmic |
|--------|------------------|-------------|
| **Collateral** | 100%+ reserves | Minimal or none |
| **Capital Efficiency** | Low (over-collateralized) | High |
| **Stability** | Proven | Experimental |
| **Decentralization** | Medium (DAI) to Low (USDC) | High |
| **Scalability** | Limited by collateral | High |
| **Primary Risk** | Collateral volatility, centralization | Death spiral, loss of confidence |
| **Complexity** | Low | High |
| **Examples** | USDC, DAI, USDT | Terra (failed), Frax, RAI |

---

**Historical Context**:

**Successes**:
- USDC, DAI maintained pegs through multiple market crashes
- Demonstrated reliability during DeFi summer (2020) and various crises

**Failures**:
- Terra/Luna (May 2022): 60B algorithmic stablecoin collapsed in days, proving death spiral risk
- Iron Finance (June 2021): TITAN token crashed, IRON lost peg
- Multiple other algorithmic experiments failed

**Current Trend**:
Industry moving toward collateral-backed models (especially fiat-backed like USDC) due to regulatory clarity and proven stability. Algorithmic experiments continue but with more caution and hybrid approaches (like Frax's fractional model).

**Grading Criteria**:
- 13 points: Comprehensive comparison with mechanisms, benefits, risks for both types
- 9-12 points: Good comparison but less detailed
- 6-8 points: Basic understanding but missing key points
- 3-5 points: Incomplete or partially incorrect
- 0-2 points: Incorrect or no meaningful answer

---

## Answer Key Summary

| Question | Type | Answer | Points |
|----------|------|--------|--------|
| Q1 | MC | B | 8 |
| Q2 | MC | C | 8 |
| Q3 | MC | B | 8 |
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

**Lectures L33-L40**:
- DeFi fundamentals and philosophy
- Automated Market Makers (AMMs) - Uniswap, Curve
- Constant product formula (x * y = k)
- Liquidity pools and impermanent loss
- Lending protocols (Aave, Compound)
- Collateralization and liquidations
- Flash loans
- Stablecoins (USDC, DAI, algorithmic)
- Yield farming and liquidity mining
- DeFi composability
- DeFi risks and security

---

## Study Recommendations

- Review lecture slides L33-L40
- Understand how AMMs work mathematically (practice x*y=k calculations)
- Study impermanent loss concept and calculations
- Know liquidation mechanisms in lending protocols
- Compare different stablecoin models (especially after Terra collapse)
- Understand composability with specific examples
- Review DeFi protocols: Uniswap, Aave, Compound, Maker
- Explore DeFi dashboards (DeFi Llama, Dune Analytics) to see real data
