!**********************************************************************
!*                                                                    *
!*      1-D Plane wave propagation with fixed and free boundaries     * 
!*                                                                    *
!**********************************************************************

!----initialzie t, dx, dt, tlen, beta, and u1, u2, u3 arrays----c

	implicit none
	integer:: i, counter, nx, nx1
	integer:: it, ntmax
	real(8):: t, dt, dt2, dx, dx2, beta, beta2, tlen, tmax, rhs
	real*8, allocatable:: u1(:), u2(:), u3(:)
	character(10):: data
	character(4):: nf
!----parameters ----c
!    dt must be less than (dx/beta) for numerical stability

	nx = 100 ! number of grid
	dt = 0.10d0 ! time interval
	dx = 1.0d0 ! grid interval
	beta = 4.0d0 ! wave velocity
	tlen = 5.0d0 ! time length of wave source
	ntmax = 1000 ! maximum time step (finish at it = ntmax, or)
	tmax = 33.0d0 ! maximum calculation time (finish at t< tmax)

!---- allocate dimension variables ----c

	nx1 = nx + 1
	allocate (u1(nx1), u2(nx1), u3(nx1))

!---- initialize t, counter, u1, u2, u3 ----c

	t = 0.0d0
	counter = 1
	
	do i = 1, nx1
		u1(i) = 0.0d0
		u2(i) = 0.0d0
		u3(i) = 0.0d0
	end do

!---- calculate c^2, dt^2, dx^2 ----c
	beta2 = beta**2
	dt2 = dt**2
	dx2 = dx**2

! ============= Time marching loop ===========
	
	do it = 1, ntmax

		t = t + dt

!---- calculate u3(i) ----c

		do i= 2, nx
			rhs=beta2*2*(u2(i+1)-2.0d0*u2(i)+u2(i-1))/dx2
			u3(i)=dt2*rhs+2.0d0*u2(i)-u1(i)
		end do

!---- free boundary (du/dx=0) ----c
		u3(1)=u3(2)
!---- fixed boundary (u=0) ----c
		u3(nx1)=0.0d0
!---- source time function c----c

		if (t.le.tlen) then
			u3(51) = sin(3.1415927*t/tlen)**2
		end if

!---- change new and old variables ----c

		do i=1,nx1
			u1(i) = u2(i)
			u2(i) = u3(i)
		end do
!---- make data file ----c
		write(nf,'(i3.3)') counter
		data = "data"//nf

		open(7,file=data,status='replace')
 		do i=1, nx1
 			write(7,*) i, u2(i)
 		end do
!---- output u2 at desired intervals, stop when t is big enough

		write(6,'(a5,1x,i3,1x,f6.3)') 'loop', counter, t
	
		if (t.gt.tmax) exit

		counter = counter + 1

	end do

	stop
	end
