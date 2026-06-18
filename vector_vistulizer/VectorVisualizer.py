import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Arc, FancyArrowPatch
import warnings
warnings.filterwarnings('ignore')

 
LIGHT = {
    "bg":      "#F8F9FC",
    "panel":   "#FFFFFF",
    "grid":    "#E2E6F0",
    "axis":    "#B0BAD0",
    "border":  "#D0D8EC",
    "text":    "#1E2A4A",
    "muted":   "#6B7A99",
    "vecA":    "#E05A2B",   # warm orange-red
    "vecB":    "#1A73E8",   # clear blue
    "vecR":    "#0FA86A",   # green  (resultant)
    "vecSub":  "#9333EA",   # purple (subtraction)
    "vecProj": "#F59E0B",   # amber  (projection)
    "vecUnit": "#64748B",   # slate  (unit vectors)
}

 
#  Math helpers
 
def mag(v):
    return np.linalg.norm(v)

def unit(v):
    m = mag(v)
    return v / m if m != 0 else v * 0

def dot_product(a, b):
    return float(np.dot(a, b))

def cross_z(a, b):
    """2-D cross product (z-component of 3-D cross)."""
    return float(a[0]*b[1] - a[1]*b[0])

def angle_deg(a, b):
    cos_t = np.clip(dot_product(a, b) / (mag(a)*mag(b)), -1, 1)
    return float(np.degrees(np.arccos(cos_t)))

def project(a, b):
    """Projection of A onto B."""
    bm = mag(b)
    if bm == 0:
        return np.zeros(2)
    return (dot_product(a, b) / bm**2) * b

def direction_deg(v):
    return float(np.degrees(np.arctan2(v[1], v[0])))  
#  Drawing helper 

def draw_vector(ax_plot, origin, vec, color, label, lw=2.5,
                linestyle='-', alpha=1.0, label_offset=(0.15, 0.15)):
    if mag(vec) < 1e-10:
        return
    ax_plot.annotate(
        "", xy=origin + vec, xytext=origin,
        arrowprops=dict(
            arrowstyle="-|>",
            color=color,
            lw=lw,
            linestyle=linestyle,
            alpha=alpha,
            mutation_scale=18,
        ),
    )
    mid = origin + vec * 0.55
    ax_plot.text(mid[0] + label_offset[0],
                 mid[1] + label_offset[1],
                 label, color=color, fontsize=11,
                 fontweight='bold', alpha=alpha,
                 bbox=dict(boxstyle='round,pad=0.2',
                           fc='white', ec=color,
                           alpha=0.85, lw=0.8))

# ─────────────────────────────────────────────
#  Main visualizer
# ─────────────────────────────────────────────

def visualize(A, B, operation='all'):
    """
    Draws up to 4 subplots depending on the chosen operation.
    operation: 'add' | 'sub' | 'dot' | 'proj' | 'unit' | 'all'
    """
    R_add = A + B
    R_sub = A - B
    proj_AB = project(A, B)   # projection of A onto B
    uA = unit(A)
    uB = unit(B)

    # ── figure layout ──────────────────────────
    fig = plt.figure(figsize=(16, 11), facecolor=LIGHT["bg"])
    fig.suptitle("Vector Visualizer ",
                 fontsize=20, fontweight='bold',
                 color=LIGHT["text"], y=0.97)

    # Subplot grid: 2 rows × 3 cols
    gs = fig.add_gridspec(2, 3, hspace=0.42, wspace=0.35,
                          left=0.05, right=0.97,
                          top=0.91, bottom=0.04)

    axes_coords = [(0,0), (0,1), (0,2), (1,0), (1,1)]
    plot_titles = [
        "A + B  (Addition)",
        "A − B  (Subtraction)",
        "Projection of A onto B",
        "Unit Vectors  (scale ×2)",
        "All Vectors Overview",
    ]
    ops_data = [
        # (vectors_list)  each: (origin, vec, color, label, lw, ls, alpha)
        [
            (np.zeros(2), A,     LIGHT["vecA"], "A",   2.5, '-', 1.0),
            (np.zeros(2), B,     LIGHT["vecB"], "B",   2.5, '-', 1.0),
            (np.zeros(2), R_add, LIGHT["vecR"], "A+B", 2.8, '-', 1.0),
        ],
        [
            (np.zeros(2), A,     LIGHT["vecA"],   "A",   2.5, '-', 1.0),
            (np.zeros(2), B,     LIGHT["vecB"],   "B",   2.5, '-', 1.0),
            (np.zeros(2), R_sub, LIGHT["vecSub"], "A-B", 2.8, '-', 1.0),
        ],
        [
            (np.zeros(2), A,       LIGHT["vecA"],    "A",          2.5, '-',  1.0),
            (np.zeros(2), B,       LIGHT["vecB"],    "B",          2.5, '-',  1.0),
            (np.zeros(2), proj_AB, LIGHT["vecProj"], "proj_B(A)",  2.5, '-',  1.0),
            (np.zeros(2), A - proj_AB,
                          LIGHT["vecSub"], "perp",  1.8, '--', 0.7),
        ],
        [
            (np.zeros(2), A,      LIGHT["vecA"],    "A",   2.0, '-',  0.5),
            (np.zeros(2), B,      LIGHT["vecB"],    "B",   2.0, '-',  0.5),
            (np.zeros(2), uA*2,   LIGHT["vecA"],    "û_A", 2.8, '-',  1.0),
            (np.zeros(2), uB*2,   LIGHT["vecB"],    "û_B", 2.8, '-',  1.0),
        ],
        [
            (np.zeros(2), A,     LIGHT["vecA"],   "A",   2.5, '-', 1.0),
            (np.zeros(2), B,     LIGHT["vecB"],   "B",   2.5, '-', 1.0),
            (np.zeros(2), R_add, LIGHT["vecR"],   "A+B", 2.0, '--',0.8),
            (np.zeros(2), R_sub, LIGHT["vecSub"], "A-B", 2.0, '--',0.8),
            (np.zeros(2), proj_AB,LIGHT["vecProj"],"proj",1.8,'--',0.7),
        ],
    ]

    for idx, ((r, c), title, vectors) in enumerate(
            zip(axes_coords, plot_titles, ops_data)):
        ax = fig.add_subplot(gs[r, c])
        ax.set_facecolor(LIGHT["panel"])
        ax.set_title(title, fontsize=10, fontweight='bold',
                     color=LIGHT["text"], pad=6)

        # Collect all endpoints to set limits
        all_pts = np.array([o + v for o, v, *_ in vectors] + [np.zeros(2)])
        xs = all_pts[:, 0]
        ys = all_pts[:, 1]
        pad = max(max(np.abs(xs).max(), np.abs(ys).max()) * 0.25, 1.5)
        xlo, xhi = xs.min() - pad, xs.max() + pad
        ylo, yhi = ys.min() - pad, ys.max() + pad

        ax.set_xlim(xlo, xhi)
        ax.set_ylim(ylo, yhi)

        # Grid
        ax.grid(True, color=LIGHT["grid"], linewidth=0.7, zorder=0)
        ax.set_axisbelow(True)

        # Axes lines
        ax.axhline(0, color=LIGHT["axis"], linewidth=1.2, zorder=1)
        ax.axvline(0, color=LIGHT["axis"], linewidth=1.2, zorder=1)

        # Spines
        for spine in ax.spines.values():
            spine.set_edgecolor(LIGHT["border"])
            spine.set_linewidth(0.8)

        ax.tick_params(colors=LIGHT["muted"], labelsize=8)
        ax.set_xlabel("X", color=LIGHT["muted"], fontsize=9)
        ax.set_ylabel("Y", color=LIGHT["muted"], fontsize=9)

        # Origin dot
        ax.plot(0, 0, 'o', color=LIGHT["text"], ms=4, zorder=5)

        # Draw vectors
        for (origin, vec, color, label, lw, ls, alpha) in vectors:
            draw_vector(ax, origin, vec, color, label, lw, ls, alpha)

        # ── angle arc on overview plot ──────────
        if idx == 4 and mag(A) > 0 and mag(B) > 0:
            ang = angle_deg(A, B)
            a1 = min(direction_deg(A), direction_deg(B))
            a2 = max(direction_deg(A), direction_deg(B))
            r_arc = min(mag(A), mag(B)) * 0.3
            arc = Arc((0, 0), 2*r_arc, 2*r_arc,
                      angle=0, theta1=a1, theta2=a2,
                      color=LIGHT["muted"], lw=1.2, linestyle=':')
            ax.add_patch(arc)
            mid_ang = np.radians((a1+a2)/2)
            ax.text(r_arc*1.3*np.cos(mid_ang),
                    r_arc*1.3*np.sin(mid_ang),
                    f"{ang:.1f}°",
                    color=LIGHT["muted"], fontsize=8)

    # ── Stats panel (bottom-right cell) ────────
    ax_stats = fig.add_subplot(gs[1, 2])
    ax_stats.set_facecolor(LIGHT["panel"])
    ax_stats.axis('off')
    ax_stats.set_title("  Analysis Report",
                       fontsize=10, fontweight='bold',
                       color=LIGHT["text"], pad=6)

    for spine in ax_stats.spines.values():
        spine.set_edgecolor(LIGHT["border"])
        spine.set_linewidth(0.8)
    ax_stats.set_xlim(0, 1)
    ax_stats.set_ylim(0, 1)

    # Draw stats table
    stats = [
        ("Vector A",         f"({A[0]:.2f}, {A[1]:.2f})",            LIGHT["vecA"]),
        ("Vector B",         f"({B[0]:.2f}, {B[1]:.2f})",            LIGHT["vecB"]),
        ("|A|  Magnitude",   f"{mag(A):.4f}",                        LIGHT["vecA"]),
        ("|B|  Magnitude",   f"{mag(B):.4f}",                        LIGHT["vecB"]),
        ("A + B",            f"({R_add[0]:.2f}, {R_add[1]:.2f})",    LIGHT["vecR"]),
        ("|A+B|",            f"{mag(R_add):.4f}",                    LIGHT["vecR"]),
        ("A − B",            f"({R_sub[0]:.2f}, {R_sub[1]:.2f})",    LIGHT["vecSub"]),
        ("|A−B|",            f"{mag(R_sub):.4f}",                    LIGHT["vecSub"]),
        ("A · B  Dot",       f"{dot_product(A,B):.4f}",              "#1E2A4A"),
        ("A × B  Cross(z)",  f"{cross_z(A,B):.4f}",                 "#1E2A4A"),
        ("Angle A,B",        f"{angle_deg(A,B):.2f}°",               "#1E2A4A"),
        ("Distance |A−B|",   f"{mag(R_sub):.4f}",                    LIGHT["vecSub"]),
        ("Direction A",      f"{direction_deg(A):.2f}°",             LIGHT["vecA"]),
        ("Direction B",      f"{direction_deg(B):.2f}°",             LIGHT["vecB"]),
        ("proj_B(A)",        f"({proj_AB[0]:.2f}, {proj_AB[1]:.2f})",LIGHT["vecProj"]),
        ("û_A  Unit",        f"({uA[0]:.3f}, {uA[1]:.3f})",         LIGHT["vecUnit"]),
        ("û_B  Unit",        f"({uB[0]:.3f}, {uB[1]:.3f})",         LIGHT["vecUnit"]),
    ]

    row_h = 1.0 / (len(stats) + 1)
    for i, (lbl, val, col) in enumerate(stats):
        y = 1.0 - (i + 1) * row_h
        # alternating row bg
        if i % 2 == 0:
            ax_stats.add_patch(
                mpatches.FancyBboxPatch((0.01, y - row_h*0.1),
                                        0.97, row_h*0.92,
                                        boxstyle="round,pad=0.005",
                                        fc="#F0F4FF", ec="none", zorder=0))
        ax_stats.text(0.04, y + row_h*0.25, lbl,
                      color=LIGHT["muted"], fontsize=7.5, va='center')
        ax_stats.text(0.96, y + row_h*0.25, val,
                      color=col, fontsize=8, fontweight='bold',
                      va='center', ha='right', fontfamily='monospace')

    # ── Console output ──────────────────────────
    print()
    print("=" * 54)
    print("       VECTOR VISUALIZER   —  RESULTS")
    print("=" * 54)
    print(f"  Vector A          : ({A[0]:.2f}, {A[1]:.2f})")
    print(f"  Vector B          : ({B[0]:.2f}, {B[1]:.2f})")
    print("-" * 54)
    print(f"  |A|  Magnitude    : {mag(A):.4f}")
    print(f"  |B|  Magnitude    : {mag(B):.4f}")
    print(f"  A + B             : ({R_add[0]:.2f}, {R_add[1]:.2f})  |{mag(R_add):.4f}|")
    print(f"  A - B             : ({R_sub[0]:.2f}, {R_sub[1]:.2f})  |{mag(R_sub):.4f}|")
    print(f"  A · B  Dot        : {dot_product(A,B):.4f}")
    print(f"  A × B  Cross(z)   : {cross_z(A,B):.4f}")
    print(f"  Angle (A, B)      : {angle_deg(A,B):.2f}°")
    print(f"  Distance |A-B|    : {mag(R_sub):.4f}")
    print(f"  Direction A       : {direction_deg(A):.2f}°")
    print(f"  Direction B       : {direction_deg(B):.2f}°")
    print(f"  Unit û_A          : ({uA[0]:.4f}, {uA[1]:.4f})")
    print(f"  Unit û_B          : ({uB[0]:.4f}, {uB[1]:.4f})")
    print(f"  proj_B(A)         : ({proj_AB[0]:.4f}, {proj_AB[1]:.4f})")
    print("=" * 54)

    plt.savefig("vector_visualizer_output.png",
                dpi=150, bbox_inches='tight',
                facecolor=LIGHT["bg"])
    print("\n    Plot saved: vector_visualizer_output.png")
    plt.show()


# ─────────────────────────────────────────────
#  Entry point
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 54)
    print("       VECTOR VISUALIZER ")
    print("       NumPy + Matplotlib  |  Light Theme")
    print("=" * 54)

    # ── Vector A ──
    print("\n  [ Vector A ]")
    ax_val = float(input("    Enter x-coordinate: "))
    ay_val = float(input("    Enter y-coordinate: "))

    # ── Vector B ──
    print("\n  [ Vector B ]")
    bx_val = float(input("    Enter x-coordinate: "))
    by_val = float(input("    Enter y-coordinate: "))

    A = np.array([ax_val, ay_val])
    B = np.array([bx_val, by_val])

    visualize(A, B)