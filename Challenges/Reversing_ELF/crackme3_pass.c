#include <stdlib.h>

int FUN_080486b0(int ptr_pass,int ptr,uint size,int param_4)

{
  uint uVar1;
  uint uVar2;
  int local_2c;
  int local_1c;
  uint local_18;
  
  local_2c = 0;
  uVar2 = size % 3;
  if (ptr == 0) {
    local_1c = (size / 3) * 4;
    if (uVar2 != 0) {
      local_1c = local_1c + 4;
    }
    if (param_4 != 0) {
      local_1c = local_1c + size / 0x39;
    }
  }
  else {
    local_1c = 0;
    for (local_18 = 0; local_18 < (size / 3) * 3; local_18 = local_18 + 3) {
      *(char *)(ptr + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [*(byte *)(ptr_pass + local_18) >> 2];
      *(char *)(local_1c + 1 + ptr) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(uint)(*(byte *)(ptr_pass + 1 + local_18) >> 4) |
            (*(byte *)(ptr_pass + local_18) & 3) << 4];
      *(char *)(local_1c + 2 + ptr) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(uint)(*(byte *)(local_18 + 2 + ptr_pass) >> 6) |
            (*(byte *)(local_18 + 1 + ptr_pass) & 0xf) * 4];
      *(char *)(local_1c + 3 + ptr) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [*(byte *)(local_18 + 2 + ptr_pass) & 0x3f];
      uVar1 = (local_1c - local_2c) + 4;
      if ((uVar1 == (uVar1 / 0x4c) * 0x4c) && (param_4 != 0)) {
        *(undefined1 *)(ptr + 4 + local_1c) = 10;
        local_1c = local_1c + 1;
        local_2c = local_2c + 1;
      }
      local_1c = local_1c + 4;
    }
    if (uVar2 == 1) {
      *(char *)(ptr + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(int)(uint)*(byte *)(ptr_pass + local_18) >> 2];
      *(char *)(ptr + 1 + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(*(byte *)(ptr_pass + local_18) & 3) * 0x10];
      *(undefined1 *)(ptr + 2 + local_1c) = 0x3d;
      *(undefined1 *)(ptr + 3 + local_1c) = 0x3d;
      local_1c = local_1c + 4;
    }
    else if (uVar2 == 2) {
      *(char *)(ptr + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(int)(uint)*(byte *)(ptr_pass + local_18) >> 2];
      *(char *)(ptr + 1 + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(int)(uint)*(byte *)(ptr_pass + 1 + local_18) >> 4 |
            (*(byte *)(ptr_pass + local_18) & 3) << 4];
      *(char *)(ptr + 2 + local_1c) =
           "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
           [(*(byte *)(ptr_pass + 1 + local_18) & 0xf) * 4];
      *(undefined1 *)(ptr + 3 + local_1c) = 0x3d;
      local_1c = local_1c + 4;
    }
  }
  return local_1c;
}

int main(void){
    printf("Chương trình tạo password của thử thách Crackme3!\n");

    return 0;
}