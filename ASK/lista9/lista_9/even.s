	.file	"even.c"
	.text
	.globl	is_even
	.type	is_even, @function
is_even:
.LFB0:
	.cfi_startproc
	endbr64
	testq	%rdi, %rdi
	je	.L2
	decq	%rdi
	jmp	is_odd@PLT
.L2:
	movl	$1, %eax
	ret
	.cfi_endproc
.LFE0:
	.size	is_even, .-is_even
	.ident	"GCC: (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0"
	.section	.note.GNU-stack,"",@progbits
	.section	.note.gnu.property,"a"
	.align 8
	.long	1f - 0f
	.long	4f - 1f
	.long	5
0:
	.string	"GNU"
1:
	.align 8
	.long	0xc0000002
	.long	3f - 2f
2:
	.long	0x3
3:
	.align 8
4:
