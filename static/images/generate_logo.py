#!/usr/bin/env python3
"""
Generate the Diagon Alley logo.
Requires: pip install Pillow
"""

from PIL import Image, ImageDraw  # type: ignore[import-not-found]

# Render at 4x size for antialiasing
scale = 4
size = 128 * scale
final_size = 128

# Consistent color scheme with Nostr Market
dark_purple = (80, 40, 120)
light_purple = (140, 100, 180)
white = (255, 255, 255)

margin = 4 * scale

swoosh_center = ((128 + 100) * scale, -90 * scale)
swoosh_radius = 220 * scale

# Create rounded rectangle mask (same as Nostr Market)
mask = Image.new("L", (size, size), 0)
mask_draw = ImageDraw.Draw(mask)
corner_radius = 20 * scale
mask_draw.rounded_rectangle(
    [margin, margin, size - margin, size - margin],
    radius=corner_radius,
    fill=255,
)

# Create background with swoosh
bg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
bg_draw = ImageDraw.Draw(bg)
bg_draw.rounded_rectangle(
    [margin, margin, size - margin, size - margin],
    radius=corner_radius,
    fill=dark_purple,
)
bg_draw.ellipse(
    [
        swoosh_center[0] - swoosh_radius,
        swoosh_center[1] - swoosh_radius,
        swoosh_center[0] + swoosh_radius,
        swoosh_center[1] + swoosh_radius,
    ],
    fill=light_purple,
)

# Apply rounded rectangle mask
final = Image.new("RGBA", (size, size), (0, 0, 0, 0))
final.paste(bg, mask=mask)
draw = ImageDraw.Draw(final)

center_x, center_y = size // 2, size // 2


def draw_shop(cx, cy, shop_scale):
    """Draw a mini shop/storefront at the given center position."""
    # Shop dimensions (scaled down from Nostr Market)
    shop_width = int(36 * scale * shop_scale)
    awning_height = int(8 * scale * shop_scale)
    body_height = int(20 * scale * shop_scale)

    shop_left = cx - shop_width // 2
    shop_right = cx + shop_width // 2

    awning_top = cy - (awning_height + body_height) // 2
    awning_bottom = awning_top + awning_height
    shop_bottom = awning_bottom + body_height
    awning_extend = int(2 * scale * shop_scale)

    # Draw awning background (white base)
    draw.rectangle(
        [
            shop_left - awning_extend,
            awning_top,
            shop_right + awning_extend,
            awning_bottom,
        ],
        fill=white,
    )

    # Vertical stripes on awning (alternating dark purple)
    stripe_count = 4
    stripe_width = (shop_width + 2 * awning_extend) // stripe_count
    for i in range(1, stripe_count, 2):
        x_left = shop_left - awning_extend + i * stripe_width
        draw.rectangle(
            [x_left, awning_top, x_left + stripe_width, awning_bottom],
            fill=dark_purple,
        )

    # Shop body (below awning)
    draw.rectangle(
        [shop_left, awning_bottom, shop_right, shop_bottom],
        fill=white,
    )

    # Display windows
    window_margin = int(3 * scale * shop_scale)
    window_top = awning_bottom + int(2 * scale * shop_scale)
    window_bottom = shop_bottom - int(2 * scale * shop_scale)
    door_half = int(3 * scale * shop_scale)

    # Left display window
    draw.rectangle(
        [shop_left + window_margin, window_top, cx - door_half, window_bottom],
        fill=dark_purple,
    )
    # Right display window
    draw.rectangle(
        [cx + door_half, window_top, shop_right - window_margin, window_bottom],
        fill=dark_purple,
    )

    # Door (center)
    draw.rectangle(
        [cx - door_half, window_top, cx + door_half, shop_bottom],
        fill=dark_purple,
    )


# Draw 4 shops in a 2x2 grid (closer together, away from edges)
offset = 26 * scale  # Offset for shop positioning
shop_size = 1.1  # Scale factor for shop size (10% bigger)

positions = [
    (center_x - offset, center_y - offset),  # Top-left
    (center_x + offset, center_y - offset),  # Top-right
    (center_x - offset, center_y + offset),  # Bottom-left
    (center_x + offset, center_y + offset),  # Bottom-right
]

for x, y in positions:
    draw_shop(x, y, shop_size)

# Downscale with LANCZOS for antialiasing
final = final.resize((final_size, final_size), Image.LANCZOS)

final.save("diagon-alley.png")
print("Logo saved to diagon-alley.png")
