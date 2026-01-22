DROP TABLE IF EXISTS bookings CASCADE;
DROP TABLE IF EXISTS listings CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- KS22Jan2026 - I know we're dropping tables with CASCADE above but just putting this line below to drop booking_details to be explicitly sure nothing is hanging around on this joint bookings_details view.

DROP VIEW IF EXISTS booking_details; 
 


DROP TYPE IF EXISTS booking_status;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name VARCHAR(255),
    description TEXT,
    price_per_night INTEGER,
    CONSTRAINT fk_user_id FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TYPE booking_status AS ENUM ('pending', 'confirmed', 'rejected');

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id INTEGER,
    guest_id INTEGER,
    date DATE,
    status booking_status DEFAULT 'pending',
    CONSTRAINT fk_listing_id FOREIGN KEY(listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    CONSTRAINT fk_guest_id FOREIGN KEY(guest_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE VIEW booking_details AS
SELECT bookings.*, 
listings.name AS listing_name, listings.description AS listing_description, listings.price_per_night
FROM bookings
JOIN listings ON listings.id = bookings.listing_id;


INSERT INTO users (email, password, name) VALUES 
    ('owner1@example.com', 'hashed_password_1', 'Property Owner 1'),
    ('owner2@example.com', 'hashed_password_2', 'Property Owner 2'),
    ('owner3@example.com', 'hashed_password_3', 'Property Owner 3'),
    ('owner4@example.com', 'hashed_password_4', 'Property Owner 4'),
    ('guest1@example.com', 'hashed_password_5', 'Guest User 1'),
    ('guest2@example.com', 'hashed_password_6', 'Guest User 2'),
    ('guest3@example.com', 'hashed_password_7', 'Guest User 3'),
    ('guest4@example.com', 'hashed_password_8', 'Guest User 4');

INSERT INTO listings (user_id, name, description, price_per_night) VALUES 
    (1, 'Cozy Canal Studio', 'Bright studio with canal views, fast WiFi, and a comfy queen bed — perfect for a weekend escape.', 95),
    (2, 'Shoreditch Loft Apartment', 'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.', 160),
    (3, 'Countryside Barn Retreat', 'Peaceful converted barn with countryside walks, a wood burner, and beautiful sunset views.', 140),
    (2, 'Luxury City Penthouse', 'Modern penthouse with skyline views, floor-to-ceiling windows, balcony seating, and premium finishes.', 320),
    (4, 'Budget-Friendly Private Room', 'Simple private room in a shared flat with great transport links — clean, safe, and ideal for solo travellers.', 55),
    (1, 'Trendy Shoreditch Studio', 'Awesome space near coffee shops and bars, great for experiencing this part of london in all its hipster glory', 145);

INSERT INTO bookings (listing_id, guest_id, date, status) VALUES
    (1, 5, '2026-03-01', 'pending'),
    (3, 8, '2026-02-14', 'confirmed'),
    (3, 3, '2026-02-14', 'confirmed'),
    (1, 3, '2026-03-23', 'pending');