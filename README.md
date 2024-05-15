# Commerce
## Video Demo: https://www.youtube.com/watch?v=EQPmgzTZXok
![Screenshot (12)](https://github.com/JuliaMaxy/project_2/assets/121096183/59c431b2-e14a-4b22-abaf-8c61abf1968a)
## Description:
The goal was to design an eBay-like e-commerce auction site that will allow users to post auction listings,
place bids on listings, comment on those listings, and add listings to a “watchlist”
## Specification:
- **`Active Listings Page`**: The default route lets users view all of the currently active auction listings.
   For each active listing, this page display the title, description, current price, and photo
- **`Create Listing`**: Users are able to visit a page to create a new listing. They should be able to specify a title for the listing,
 a text-based description, and what the starting bid should be, an image for the listing, condition of the item and a category
- **`Listing Page`**: Clicking on a listing takes users to a page specific to that listing.
   On that page, users are able to view all details about the listing, including the current price for the listing.
  - If the user is signed in, the user can add the item to their `Watchlist` If the item is already on the watchlist, the user can remove it.
  - If the user is signed in, the user can bid on the item.
   The bid must be at least as large as the starting bid, and must be greater than any other bids that have been placed (if any).
   If the bid doesn’t meet those criteria, the user is presented with an error.
  - If the user is signed in and is the one who created the listing, the user has the ability to “close” the auction from this page,
   which makes the highest bidder the winner of the auction and makes the listing no longer active.
  - If a user is signed and listing is closed, the user can view who won the auction(if anyone) on the `closed auctions` page.
  - Users who are signed in are able to add comments to the listing page.
    The listing page displays all comments that have been made on the listing.
- **`Watchlist`**: Users who are signed in are able to visit a Watchlist page, which displays all of the listings that a user has added to their watchlist.
  Clicking on any of those listings takes the user to that listing’s page.
- **`Categories`**: Users are able to visit a page that displays a list of all listing categories.
  Clicking on the name of any category takes the user to a page that displays all of the active listings in that category.

