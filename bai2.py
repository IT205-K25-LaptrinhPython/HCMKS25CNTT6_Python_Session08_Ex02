# Phân tích Input/Output
# Dữ liệu đầu vào
# Tất cả các dữ liệu đầu vào đều là Kiểu chuỗi (String).
# Menu hệ thống: Lựa chọn chức năng (choice): Các ký tự từ "1" đến "5".
# Chức năng 1 (Nhập thông tin):
# Tên shop (shop_name)
# Tên sản phẩm (product_name)
# Mô tả sản phẩm (description)
# Danh mục sản phẩm (category)
# Danh sách từ khóa tìm kiếm (keywords - nhập cách nhau bằng dấu phẩy)
# Chức năng 3 (Kiểm tra mã giảm giá): * Mã giảm giá (discount_code)
# Chức năng 4 (Tìm và thay thế): * Từ khóa cần tìm (find_word)
# Từ khóa thay thế (replace_word)
# Dữ liệu đầu ra (Output)
# Chức năng 1:
# Các thông tin được chuẩn hóa khoảng trắng (Tên shop, Tên sản phẩm, Mô tả, Danh mục).
# Tên sản phẩm viết hoa chữ cái đầu.
# Các thông số phân tích: Độ dài mô tả, số lượng từ khóa.
# Chuỗi mô tả ở định dạng in HOA và in thường toàn bộ.
# Chức năng 2: Tên shop ban đầu và tên đã được chuẩn hóa (Thêm shop- ở đầu và thay khoảng trắng bằng gạch ngang).
# Chức năng 3:
# Thông báo lỗi cụ thể nếu mã giảm giá không hợp lệ (rỗng, chứa khoảng trắng, sai độ dài, không in hoa, chứa ký tự đặc biệt, không bắt đầu bằng SALE).
# Thông báo thành công và chuỗi danh sách mã giảm giá nếu hợp lệ.
# Chức năng 4: Số lượng từ khóa tìm thấy và thực hiện thay thế ngầm trong biến mô tả.
# Thông báo "Không tìm thấy" nếu từ khóa không tồn tại.
# Chức năng 5: Dòng thông báo thoát và ngắt chương trình.

# Đề xuất giải pháp
# Để giải quyết bài toán, chương trình sử dụng cấu trúc lặp kết hợp rẽ nhánh và các phương thức xử lý chuỗi (String methods) cốt lõi của Python.
# Cấu trúc điều khiển chính
# Vòng lặp while True: Tạo một vòng lặp vô hạn để hiển thị menu liên tục.
# Câu lệnh match-case: Dùng để điều hướng luồng thực thi tương ứng với các lựa chọn từ 1 đến 5 
# (có thêm case _ để bẫy lỗi nhập sai lựa chọn).
# Các phương thức xử lý chuỗi và kiểm tra dữ liệu (Không dùng mảng)
# Làm sạch và định dạng văn bản: * .strip(): Cắt bỏ khoảng trắng ở đầu và cuối chuỗi.
# .title(): Viết hoa chữ cái đầu của mỗi từ.
# .upper() / .lower(): Chuyển đổi toàn bộ chuỗi sang in hoa / in thường.
# .replace(" ", "-"): Thay thế khoảng trắng bằng dấu gạch ngang (dùng kết hợp vòng lặp để xóa khoảng trắng thừa).
# Nối chuỗi: Dùng phép cộng (+) để gom các mã giảm giá vào một chuỗi duy nhất.
# Kiểm tra tính hợp lệ (Validation):
# Kiểm tra rỗng: Dùng len(string) == 0.
# Kiểm tra tiền tố: Dùng .startswith("SALE") hoặc .startswith("shop-").
# Kiểm tra định dạng: Dùng .isupper() (viết hoa) và .isalnum() (chỉ chứa chữ và số).
# Kiểm tra chứa ký tự: Dùng toán tử in.
# Tìm kiếm và thay thế: .replace(old, new) và .count(word).

# Thiết kế thuật toán (Pseudocode)
# BẮT ĐẦU CHƯƠNG TRÌNH
# LẶP VÔ HẠN (while True):
#     IN ra màn hình Khung giao diện Menu (1 đến 5)
#     NHẬP lựa chọn chức năng vào biến 'choice'    
#     CHỌN 'choice':
#         TRƯỜNG HỢP "1":
#             NHẬP shop_name, product_name, description, category, keywords
#             NẾU shop_name rỗng HOẶC description rỗng:
#                 IN thông báo lỗi và TIẾP TỤC (continue) vòng lặp            
#             LÀM SẠCH và ĐỊNH DẠNG:
#                 IN shop_name, product_name, description, category (đã xử lý khoảng trắng và format)
#             TÍNH TOÁN:
#                 IN độ dài chuỗi description
#                 TÍNH số lượng từ khóa bằng cách đếm dấu phẩy (.count(",") + 1)
#                 IN description in hoa và in thường           
#         TRƯỜNG HỢP "2":
#             IN shop_name ban đầu
#             CHUYỂN shop_name thành chữ thường
#             LẶP XÓA khoảng trắng thừa (replace "  " thành " ")
#             THAY THẾ khoảng trắng bằng "-"
#             NẾU chưa có "shop-": THÊM "shop-"
#             IN shop_name đã chuẩn hóa       
#         TRƯỜNG HỢP "3":
#             NHẬP discount_code
#             NẾU discount_code rỗng: IN lỗi rỗng
#             NGƯỢC LẠI NẾU có chứa khoảng trắng: IN lỗi khoảng trắng
#             NGƯỢC LẠI NẾU độ dài không từ 6 đến 12: IN lỗi độ dài
#             NGƯỢC LẠI NẾU không viết hoa toàn bộ: IN lỗi viết hoa
#             NGƯỢC LẠI NẾU không chỉ chứa chữ và số: IN lỗi định dạng
#             NGƯỢC LẠI NẾU không bắt đầu bằng "SALE": IN lỗi tiền tố
#             NGƯỢC LẠI:
#                 IN "Mã giảm giá hợp lệ"
#                 NỐI discount_code vào chuỗi str_discount_codes
#                 IN chuỗi mã giảm giá          
#         TRƯỜNG HỢP "4":
#             NHẬP find_word và replace_word
#             ĐẾM số lần xuất hiện của find_word trong description (count_word)
#             NẾU count_word > 0:
#                 THAY THẾ find_word bằng replace_word trong description
#                 IN count_word
#             NGƯỢC LẠI:
#                 IN "Không tìm thấy"           
#         TRƯỜNG HỢP "5":
#             IN "Thoát chương trình"
#             THOÁT LẶP (break)         
#         TRƯỜNG HỢP MẶC ĐỊNH (Khác 1-5):
#             IN "Lựa chọn không hợp lệ"
# KẾT THÚC CHƯƠNG TRÌNH


while True:
    print(f"+{"="*68}+")
    print("|            HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE               |")
    print(f"+{"="*68}+")
    print("|   1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê                 |")
    print("|   2. Chuẩn hóa tên shop                                            |")
    print("|   3. Kiểm tra mã giảm giá hợp lệ                                   |")
    print("|   4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm             |")
    print("|   5. Thoát chương trình                                            |")
    print(f"+{"="*68}+")
    
    choice = input("> Mời bạn chọn chức năng (1-5): ")
    
    match choice:
        case "1":
            shop_name = input("Nhập tên shop: ")
            if (len(shop_name.strip()) == 0):
                print("Tên shop không được bỏ trống")
                continue            
            product_name = input("Nhập tên sản phẩm: ")            
            description = input("Nhập mô tả sản phẩm: ")
            if (len(description.strip()) == 0):
                print("Mô tả sản phẩm không được rỗng")
                continue           
            category = input("Nhập danh mục sản phẩm: ")
            keywords = input("Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")
            print()            
            print(f"Tên shop: {shop_name.strip()}")
            print(f"Tên sản phẩm: {product_name.strip().title()}")
            print(f"Mô tả sản phẩm: {description.strip()}")
            print(f"Độ dài mô tả sản phẩm: {len(description.strip())}")
            print(f"Danh mục sản phẩm: {category.strip().lower()}")            
            keywords_clean = keywords.replace(" ", "")
            print(f"Danh sách từ khóa sau khi chuẩn hóa: {keywords_clean}")
            if len(keywords_clean) > 0:
                count_keywords = keywords_clean.count(",") + 1
            else:
                count_keywords = 0
            print(f"Số lượng từ khóa tìm kiếm: {count_keywords}")
            print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ thường: {description.lower()}")
            print(f"Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa: {description.upper()}")
            print()           
        case "2":
            print(f"Tên shop ban đầu: {shop_name}")
            normalized_shop = shop_name.lower().strip()
            normalized_shop = normalized_shop.replace(" ", "-")
            if not normalized_shop.startswith("shop-"):
                normalized_shop = "shop-" + normalized_shop
            print(f"Tên shop sau khi được chuẩn hóa: {normalized_shop}")
            print()
        case "3":
            discount_code = input("Nhập vào mã giảm giá: ")
            if (len(discount_code) == 0):
                print("Mã giảm giá không được rỗng")
            elif (" " in discount_code):
                print("Mã giảm giá không được chứa khoảng trắng")
            elif (len(discount_code) < 6 or len(discount_code) > 12):
                print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
            elif (not discount_code.isupper()):
                print("Mã giảm giá phải được viết hoa toàn bộ")
            elif (not discount_code.isalnum()):
                print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
            elif (not discount_code.startswith("SALE")):
                print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")
            else:
                print("Mã giảm giá hợp lệ!")
                if len(str_discount_codes) == 0:
                    str_discount_codes = discount_code
                else:
                    str_discount_codes = str_discount_codes + ", " + discount_code           
                print(f"Danh sách mã giảm giá hiện tại: {str_discount_codes}")
            print()   
        case "4":
            find_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")            
            count_word = description.count(find_word)            
            if (count_word > 0):
                print(f"Số lần xuất hiện của từ khóa: {count_word}")
                description = description.replace(find_word, replace_word)
                print(f"Mô tả sau khi thay thế:\n{description}")
            else:
                print("Không tìm thấy")
            print()           
        case "5":
            print("Thoát chương trình\n")
            break           
        case _:
            print("Lựa chọn không hợp lệ\n")