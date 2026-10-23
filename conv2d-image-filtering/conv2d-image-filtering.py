
import math

def pad_image(image: list, padding: int = 0) -> list:
    if not image:
        return []

    h_in = len(image)
    w_in = len(image[0])

    if padding == 0:
        return [row[:] for row in image]

    padded_width = w_in + 2 * padding

    ans = [[0] * padded_width for _ in range(padding)]

    for row in image:
        ans.append([0] * padding + row[:] + [0] * padding)

    ans.extend([[0] * padded_width for _ in range(padding)])

    return ans


def conv2d(
    image: list,
    kernel: list,
    stride: int = 1,
    padding: int = 0
) -> list:
    """
    Perform a 2D cross-correlation (the operation commonly called
    convolution in deep learning frameworks).

    Args:
        image: 2D input matrix.
        kernel: 2D kernel.
        stride: Step size of the kernel.
        padding: Number of zero-padding rows and columns on each side.

    Returns:
        A 2D list containing the output.
    """
    if not image or not image[0] or not kernel or not kernel[0]:
        raise ValueError("Image and kernel must be non-empty.")

    if stride <= 0 or padding < 0:
        raise ValueError("Stride must be positive and padding non-negative.")

    if any(len(row) != len(image[0]) for row in image):
        raise ValueError("Image must be rectangular.")

    if any(len(row) != len(kernel[0]) for row in kernel):
        raise ValueError("Kernel must be rectangular.")

    X = pad_image(image, padding)

    h_in = len(image)
    w_in = len(image[0])

    k_h = len(kernel)
    k_w = len(kernel[0])

    h_out = math.floor((h_in + 2 * padding - k_h) / stride) + 1
    w_out = math.floor((w_in + 2 * padding - k_w) / stride) + 1

    if h_out <= 0 or w_out <= 0:
        raise ValueError("Kernel is larger than the padded image.")

    ans = [[0] * w_out for _ in range(h_out)]

    for i in range(h_out):
        for j in range(w_out):
            for a in range(k_h):
                for b in range(k_w):
                    ans[i][j] += (
                        X[i * stride + a][j * stride + b]
                        * kernel[a][b]
                    )

    return ans