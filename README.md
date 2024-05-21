# Python-Blackjack

Blackjack, also known as 21, is a card game that is usually played by two people, but could be more (if played casually).
The main objective of the game is to get 21 as the sum of the cards number in your hand. If your sum is higher than the sum of the other person, you win the game, but if your sum goes over 21, you lose.
The game starts with you and let's call, the dealer, receiving two cards each. After that, you see your cards, but only see one card of the dealer. It's up to you to get another card or stop there. If you get another card and your sum is higher than 21, boom, you lose. If you stop, the dealer will shown his cards, and if the value of it is lower than 17, the dealer must pick up new cards, until the sum is higher than 17. Then the same rules goes to the dealer. If the card that he picks before the sum is over 17 leads him to a sum higher than 21, he automatically loses. But if not, the you two compare each other sum. If your sum is higher, you win, and if the dealer's sum is higher, you lose. If the sums are equal, it's a draw. If you get a blackjack (a sum of 21) on the first round with your two cards, you win.
The cards are:
Ace
1
2
3
4
5
6
7
8
9
10
Q
J
K

The ace value can be 1 or 11, depending on your situation.
Q, J and K value 10.

In the code, the "cards" list represents the values of the cards. The "11" is the ace, that becomes "1" in some specific situations (if sum is higher than 21)
