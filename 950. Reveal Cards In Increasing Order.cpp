// https://leetcode.com/problems/reveal-cards-in-increasing-order/

// In a deck of cards, every card has a unique integer.  You can order the deck in
// any order you want.

// Initially, all the cards start face down (unrevealed) in one deck.

// Now, you do the following steps repeatedly, until all cards are revealed:

// Return an ordering of the deck that would reveal the cards in increasing order.

// The first entry in the answer is considered to be the top of the deck.

////////////////////////////////////////////////////////////////////////////////

class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        // simulate idxes
        int n = deck.size();
        queue<int> idxes; for (int i = 0; i < n; ++i) idxes.push(i);
        vector<int> ans(n);
        sort(deck.begin(), deck.end());
        
        for (int& card : deck) {
            // reveal an index, set ans[indx] = current smallest card
            int idx = idxes.front(); idxes.pop();
            ans[idx] = card;
            if (!idxes.empty()) {
                idxes.push(idxes.front()); idxes.pop(); // put front card to back
            }
        }
        return ans;
    }
};
