DROP TABLE IF EXISTS listings CASCADE;
DROP TABLE IF EXISTS bookings CASCADE;
DROP TYPE IF EXISTS booking_status;

CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    name VARCHAR(255),
    description TEXT,
    price_per_night INTEGER
);

INSERT INTO listings (user_id, name, description, price_per_night) VALUES 
    (1, 'Cozy Canal Studio', 'Bright studio with canal views, fast WiFi, and a comfy queen bed — perfect for a weekend escape.', 95),
    (2, 'Shoreditch Loft Apartment', 'Trendy open-plan loft in the heart of Shoreditch, minutes from coffee spots, nightlife, and the Tube.', 160),
    (3, 'Countryside Barn Retreat', 'Peaceful converted barn with countryside walks, a wood burner, and beautiful sunset views.', 140),
    (2, 'Luxury City Penthouse', 'Modern penthouse with skyline views, floor-to-ceiling windows, balcony seating, and premium finishes.', 320),
    (4, 'Budget-Friendly Private Room', 'Simple private room in a shared flat with great transport links — clean, safe, and ideal for solo travellers.', 55),
    (1, 'Trendy Shoreditch Studio', 'Awesome space near coffee shops and bars, great for experiencing this part of london in all its hipster glory', 145);


CREATE TYPE booking_status AS ENUM ('pending', 'confirmed', 'rejected');

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    listing_id INTEGER,
    guest_id INTEGER,
    date DATE,
    status booking_status DEFAULT 'pending'
);